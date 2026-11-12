"""Nodo SUPERVISOR: el director de tráfico. Decide quién trabaja ahora (o si se cierra) y con qué instrucción.

No ejecuta trabajo: no busca, no calcula y no redacta. Tampoco lee el historial de mensajes: lee
un TABLERO armado de forma determinística desde el estado (qué entregó cada especialista, la
rúbrica de suficiencia, las correcciones pendientes y el último rechazo del validador). Así su
prompt no crece con cada vuelta y los especialistas no le contaminan el contexto.

La decisión es una salida estructurada `DecisionSupervisor` con `siguiente: Literal[...]`; la
arista condicional `ruta_supervisor` (graph.py) la mapea al nodo.

Guardas determinísticas sobre la decisión del LLM (quedan registradas en `aportes`):
1. límite de pasos: la última decisión es siempre "finalizar", sin consultar al LLM;
2. dependencias: analista sin investigación -> investigador; crítico sin análisis -> analista;
3. especialista que agotó sus intentos -> el siguiente pendiente de la rúbrica (o finalizar);
4. insistir en finalizar después de un rechazo del validador, con algo resoluble -> ese pendiente;
5. salida inválida del LLM -> plan B: el siguiente pendiente de la rúbrica.
"""

import functools
import logging
from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.runnables import Runnable
from pydantic import BaseModel, Field

from agents.analyst_agent import resumen_calculos
from config import DDSettings
from corpus import Corpus
from llm import es_error_del_proveedor, es_reintentable
from state import AGENTES, Aporte, Destino, EstadoDD
from validation import evaluar, formatear_rubrica, siguiente_pendiente

logger = logging.getLogger(__name__)

PROMPT = """\
Sos el SUPERVISOR de un equipo de due diligence de startups de IA para un fondo de inversión.
Tu único trabajo es COORDINAR: decidir qué especialista trabaja ahora y con qué instrucción, o cerrar.
NO investigás, NO calculás y NO redactás el informe.

Especialistas:
- investigador: busca en el data room y en fuentes de mercado; registra métricas (con cita literal de
  la fuente) y hallazgos cualitativos. Es el ÚNICO que puede agregar o cambiar un dato.
- analista: con herramientas calcula costo de LLM, unit economics, tamaño de mercado y scoring.
  Solo usa métricas registradas por el investigador.
- critico: audita. Contrasta lo declarado con lo calculado, busca letra chica y registra red flags
  (riesgos de la startup) y correcciones (errores del equipo, dirigidas a un agente).

Orden natural: investigador -> analista -> critico -> (correcciones al agente afectado) -> finalizar.

Rúbrica de suficiencia: está en el tablero y la aplica el validador antes de cerrar. Un punto [ ]
bloquea el cierre; un punto [!] es una salvedad que no bloquea.

Cómo decidir:
- Si hay correcciones de severidad alta pendientes, mandalas al agente afectado citando la corrección
  (primero al investigador si cambia un dato: después el analista tiene que recalcular).
- Si el análisis quedó viejo (la investigación cambió), mandá al analista. Si la crítica quedó vieja
  (el análisis cambió), mandá al crítico para que re-audite.
- Si el validador rechazó el cierre, resolvé los errores que listó.
- No vuelvas a llamar a un especialista que agotó sus intentos.
- Elegí "finalizar" cuando la rúbrica no tiene puntos [ ] o cuando nadie puede aportar algo nuevo.
- La instrucción tiene que ser específica y autocontenida: el especialista NO ve este tablero, solo
  tu instrucción (qué hacer, qué datos faltan, qué corrección aplicar).
"""


class DecisionSupervisor(BaseModel):
    """Decisión del supervisor: quién trabaja ahora, o si se cierra el análisis."""

    razonamiento: str = Field(description="Por qué elegís este paso, en 1 o 2 oraciones, citando la rúbrica.")
    siguiente: Destino = Field(description="El especialista que trabaja ahora, o 'finalizar'.")
    instruccion: str = Field(description="Instrucción específica y autocontenida para el especialista (vacía si es 'finalizar').")


def _pedido(state: EstadoDD) -> str:
    return next((m.text for m in state["messages"] if isinstance(m, HumanMessage)), "")


def tablero(state: EstadoDD, settings: DDSettings, nombre_startup: str) -> str:
    """Resumen del estado para decidir: lo que el supervisor necesita y nada más."""
    inv, ana, cri, val = state.get("investigacion"), state.get("analisis"), state.get("critica"), state.get("validacion")
    intentos = state.get("intentos", {})

    def cupo(agente: str) -> str:
        return f"{intentos.get(agente, 0)}/{settings.max_intentos(agente)}"

    if inv:
        faltan = inv.faltantes()
        estado_inv = (
            f"v{inv.version}: {len(inv.metricas)} métricas ancladas, {len(inv.hallazgos)} hallazgos, "
            f"{inv.rechazos} registros rechazados. Faltan: {', '.join(faltan) or 'ninguna'}."
        )
    else:
        estado_inv = "sin entregar."
    estado_ana = f"v{ana.version} (con la investigación v{ana.version_investigacion}): {resumen_calculos(ana)}." if ana else "sin entregar."
    if cri:
        altas = sum(r.severidad == "alta" for r in cri.red_flags)
        estado_cri = f"v{cri.version} (auditó el análisis v{cri.version_analisis}): {len(cri.red_flags)} red flags ({altas} altas), {len(cri.correcciones)} correcciones emitidas."
    else:
        estado_cri = "sin revisar."

    pendientes = []
    if cri:
        atendidas = {
            "investigador": inv.correcciones_atendidas if inv else [],
            "analista": ana.correcciones_atendidas if ana else [],
        }
        pendientes = [c for c in cri.correcciones if c.id not in atendidas[c.agente_afectado]]
    lineas_pendientes = "\n".join(f"- {c.id} ({c.severidad}) -> {c.agente_afectado}: {c.descripcion}" for c in pendientes) or "(ninguna)"

    validacion = "todavía no se intentó cerrar."
    if val is not None:
        validacion = (
            "aprobada."
            if val.aprobado
            else f"RECHAZADA en el intento {val.intento}: " + "; ".join(f"{c.nombre}: {c.detalle}" for c in val.errores)
        )
    decisiones = "\n".join(f"- paso {a.paso}: {a.accion}" for a in state.get("aportes", []) if a.agente == "supervisor") or "(ninguna)"

    return f"""\
STARTUP: {nombre_startup} (id: {state["startup"]})
PEDIDO DEL USUARIO: {_pedido(state)}
PASO: {state["pasos"] + 1} de {settings.max_pasos}

ESPECIALISTAS (intentos usados/máximo):
- investigador ({cupo("investigador")}): {estado_inv}
- analista ({cupo("analista")}): {estado_ana}
- critico ({cupo("critico")}): {estado_cri}

RÚBRICA DE SUFICIENCIA:
{formatear_rubrica(evaluar(state, settings))}

CORRECCIONES PENDIENTES:
{lineas_pendientes}

ÚLTIMA VALIDACIÓN: {validacion}

DECISIONES ANTERIORES:
{decisiones}"""


def aplicar_guardas(state: EstadoDD, settings: DDSettings, destino: Destino, instruccion: str) -> tuple[Destino, str, str | None]:
    """Corrige la decisión del LLM cuando viola una regla dura. Devuelve (destino, instrucción, regla aplicada)."""
    intentos = state.get("intentos", {})
    if destino == "analista" and state.get("investigacion") is None:
        return "investigador", "Relevá el data room completo y el tamaño de mercado.", "dependencia: no hay investigación para analizar"
    if destino == "critico" and state.get("analisis") is None:
        alternativo: Destino = "analista" if state.get("investigacion") else "investigador"
        return alternativo, "", "dependencia: no hay análisis para auditar"
    if destino in AGENTES and intentos.get(destino, 0) >= settings.max_intentos(destino):
        alternativo, detalle = siguiente_pendiente(state, settings)
        return alternativo, detalle, f"{destino} agotó sus {settings.max_intentos(destino)} intentos"
    if destino == "finalizar" and (val := state.get("validacion")) is not None and not val.aprobado:
        alternativo, detalle = siguiente_pendiente(state, settings)
        if alternativo != "finalizar":
            return alternativo, detalle, "el validador rechazó el cierre y hay un punto resoluble"
    return destino, instruccion, None


def crear_nodo_supervisor(model: BaseChatModel, corpus: Corpus, settings: DDSettings, *, reintentos_llm: int = 0):
    @functools.cache
    def decisor() -> Runnable:
        # Se arma en la primera decisión: construir el grafo (por ejemplo, para dibujarlo) no exige un modelo real.
        # method="json_schema": los Claude 5.5 rechazan el tool_choice forzado del modo por defecto.
        estructurado = model.with_structured_output(DecisionSupervisor, method="json_schema")
        if reintentos_llm:
            estructurado = estructurado.with_retry(
                retry_if_exception_type=es_reintentable, stop_after_attempt=reintentos_llm + 1, wait_exponential_jitter=True
            )
        return estructurado

    async def decidir(state: EstadoDD) -> DecisionSupervisor:
        mensajes = [SystemMessage(PROMPT), HumanMessage(tablero(state, settings, corpus.startups[state["startup"]]))]
        decision = await decisor().ainvoke(mensajes, {"tags": ["agente:supervisor"], "run_name": "supervisor"})
        if not isinstance(decision, DecisionSupervisor):
            raise ValueError(f"salida estructurada vacía o inválida: {decision!r}")
        return decision

    async def supervisor(state: EstadoDD) -> dict[str, Any]:
        paso = state["pasos"] + 1
        reglas: list[str] = []
        if paso >= settings.max_pasos:
            destino, instruccion, razonamiento = "finalizar", "", f"Se alcanzó el límite de {settings.max_pasos} pasos."
            reglas.append("límite de pasos")
        else:
            try:
                decision = await decidir(state)
                destino, instruccion, razonamiento = decision.siguiente, decision.instruccion.strip(), decision.razonamiento.strip()
            except Exception as exc:
                if es_error_del_proveedor(exc):
                    raise  # auth, cuota o red: no tiene sentido seguir sin LLM
                logger.warning("Decisión inválida del supervisor (%s): plan B por rúbrica", exc)
                destino, instruccion = siguiente_pendiente(state, settings)
                razonamiento = f"Plan B: la salida del LLM fue inválida ({type(exc).__name__})."
                reglas.append("plan B por rúbrica")
            destino, instruccion, regla = aplicar_guardas(state, settings, destino, instruccion)
            if regla:
                reglas.append(regla)
        if destino != "finalizar" and not instruccion:
            instruccion = siguiente_pendiente(state, settings)[1] or "Completá tu parte de la due diligence."

        intentos = dict(state.get("intentos", {}))
        if destino != "finalizar":
            intentos[destino] = intentos.get(destino, 0) + 1
        detalle = razonamiento + (f" [guarda: {'; '.join(reglas)}]" if reglas else "")
        if reglas:
            logger.info("Supervisor, paso %d: guarda aplicada (%s) -> %s", paso, "; ".join(reglas), destino)
        return {
            "siguiente": destino,
            "instruccion": instruccion,
            "pasos": paso,
            "intentos": intentos,
            "motivo_cierre": razonamiento if destino == "finalizar" else "",
            "aportes": [Aporte(paso=paso, agente="supervisor", accion=f"→ {destino}", detalle=detalle)],
            "messages": [AIMessage(content=f"→ {destino}: {instruccion or razonamiento}", name="supervisor")],
        }

    return supervisor
