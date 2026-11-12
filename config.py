"""Configuración del orquestador: rutas y frenos contra el "supervisor infinito".

Tres frenos complementarios:
- `max_pasos` (blando): decisiones del supervisor por análisis. Al llegar, el supervisor cierra
  sin consultar al LLM y el validador decide si el informe sale con recomendación o se abstiene.
- `max_intentos_*`: veces que se puede delegar en cada especialista. Corta el bucle
  crítico ↔ analista ("el crítico siempre encuentra algo").
- `recursion_limit` (duro): techo de super-pasos de LangGraph. Cada paso del supervisor consume
  2 (supervisor + especialista); debe superar 2 × max_pasos + 3 para que los blandos actúen antes.

Dentro de cada especialista, `max_iteraciones_especialista` limita las rondas de herramientas
de su ciclo ReAct (el mismo freno de la PE5).
"""

import os
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator

BASE_DIR = Path(__file__).resolve().parent


class DDSettings(BaseModel):
    data_dir: Path = BASE_DIR / "data"
    informes_dir: Path = BASE_DIR / "informes"
    trazas_dir: Path = BASE_DIR / "trazas"
    max_pasos: int = Field(default=12, ge=4, le=30, description="Decisiones del supervisor por análisis")
    max_intentos_investigador: int = Field(default=3, ge=1, le=5)
    max_intentos_analista: int = Field(default=3, ge=1, le=5)
    max_intentos_critico: int = Field(default=2, ge=1, le=5)
    rondas_para_no_disponible: int = Field(
        default=2, ge=1, le=5, description="Búsquedas del investigador tras las que una métrica faltante se da por no disponible"
    )
    max_iteraciones_especialista: int = Field(
        default=6, ge=1, le=10, description="Rondas de herramientas por invocación (el analista necesita 4 en secuencia)"
    )
    recursion_limit: int = Field(default=40, ge=10, le=200)
    minimo_metricas: int = Field(default=6, ge=1, description="Métricas ancladas mínimas para dar por buena la investigación")
    minimo_hallazgos: int = Field(default=2, ge=0, description="Hallazgos cualitativos con cita mínimos")
    modelo_supervisor: str | None = Field(
        default=None, description="Modelo propio para el supervisor (opcional; por defecto el mismo que los especialistas)"
    )

    @field_validator("data_dir", "informes_dir", "trazas_dir")
    @classmethod
    def resolver_ruta(cls, ruta: Path) -> Path:
        return ruta if ruta.is_absolute() else BASE_DIR / ruta

    @model_validator(mode="after")
    def frenos_coherentes(self) -> "DDSettings":
        if self.recursion_limit <= 2 * self.max_pasos + 3:
            raise ValueError("recursion_limit debe ser mayor que 2 * max_pasos + 3")
        return self

    def max_intentos(self, agente: str) -> int:
        return getattr(self, f"max_intentos_{agente}")


def describir_error_config(exc: ValidationError) -> str:
    """Primer error de validación en una línea, con el campo que lo causó (si lo hay)."""
    primero = exc.errors()[0]
    campo = ".".join(str(parte) for parte in primero["loc"])
    mensaje = primero["msg"].removeprefix("Value error, ")
    sufijo = "" if ".env" in mensaje else " (revisá el .env)"
    return f"Configuración inválida: {campo + ': ' if campo else ''}{mensaje}{sufijo}"


def dd_settings_from_env(**overrides: Any) -> DDSettings:
    variables = {
        "max_pasos": "DD_MAX_PASOS",
        "max_intentos_investigador": "DD_MAX_INTENTOS_INVESTIGADOR",
        "max_intentos_analista": "DD_MAX_INTENTOS_ANALISTA",
        "max_intentos_critico": "DD_MAX_INTENTOS_CRITICO",
        "max_iteraciones_especialista": "DD_MAX_ITERACIONES_ESPECIALISTA",
        "recursion_limit": "DD_RECURSION_LIMIT",
        "modelo_supervisor": "DD_MODELO_SUPERVISOR",
    }
    data = {campo: os.getenv(var) for campo, var in variables.items()}
    data = {k: v for k, v in data.items() if v not in (None, "")}
    data.update(overrides)
    return DDSettings.model_validate(data)
