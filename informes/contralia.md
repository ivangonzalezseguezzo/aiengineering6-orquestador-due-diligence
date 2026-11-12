# Due diligence — Contralia

Fecha: 2026-11-11 · Decisiones del supervisor: 4 · Validación: aprobada

## Recomendación preliminar: AVANZAR A COMITÉ

Motivo: score 92,0/100 (banda: avanzar a comité).

> Recomendación generada por el sistema a partir de datos anclados a sus fuentes. La decisión de invertir la toma el comité con aprobación humana explícita (la PE7 agrega ese paso al flujo).

## Métricas registradas (investigador)

| Métrica | Valor | Fuente | Cita |
|---|---|---|---|
| mrr_usd | 85.500 | contralia/metricas#1 | "MRR (ingreso recurrente mensual): USD 85.500" |
| clientes_activos | 90 | contralia/metricas#1 | "Clientes pagos activos con contrato recurrente: 90" |
| crecimiento_mrr_mensual_pct | 8,5 | contralia/metricas#1 | "Crecimiento mensual promedio del MRR (últimos 6 meses): 8,5 %" |
| churn_mensual_pct | 1,8 | contralia/metricas#2 | "Churn mensual de clientes (promedio de los últimos 6 meses): 1,8 %" |
| concentracion_top_cliente_pct | 7 | contralia/clientes-y-equipo#1 | "El cliente más grande representa el 7 % del MRR" |
| gasto_comercial_mensual_usd | 52.000 | contralia/finanzas#3 | "Gasto mensual en ventas y marketing: USD 52.000" |
| clientes_nuevos_mes | 8 | contralia/metricas#3 | "Clientes nuevos por mes (promedio de los últimos 6 meses): 8" |
| costo_infra_mensual_usd | 6.800 | contralia/finanzas#1 | "Infraestructura cloud (sin incluir el LLM): USD 6.800 por mes" |
| otros_costos_directos_mensual_usd | 11.500 | contralia/finanzas#1 | "Otros costos directos (soporte y onboarding de clientes): USD 11.500 por mes" |
| margen_bruto_declarado_pct | 72 | contralia/finanzas#2 | "Margen bruto declarado: 72 %" |
| burn_neto_mensual_usd | 48.000 | contralia/finanzas#4 | "Burn neto mensual: USD 48.000" |
| caja_usd | 1.150.000 | contralia/finanzas#4 | "Caja disponible al 31/10/2026: USD 1.150.000" |
| runway_declarado_meses | 24 | contralia/finanzas#4 | "Runway declarado: 24 meses, sin contar la ronda que estamos levantando" |
| llamadas_llm_mes | 520.000 | contralia/tecnologia#2 | "Llamadas al LLM por mes: 520.000" |
| tokens_entrada_por_llamada | 4.000 | contralia/tecnologia#2 | "Tokens de entrada promedio por llamada: 4.000" |
| tokens_salida_por_llamada | 700 | contralia/tecnologia#2 | "Tokens de salida promedio por llamada: 700" |
| precio_entrada_usd_millon | 1,25 | contralia/tecnologia#3 | "Precio por millón de tokens de entrada: USD 1,25" |
| precio_salida_usd_millon | 10 | contralia/tecnologia#3 | "Precio por millón de tokens de salida: USD 10" |
| clientes_potenciales_tam | 21.000 | mercado/legaltech-latam#1 | "Organizaciones objetivo (departamentos legales de empresas medianas y grandes, más estudios con 10 o
  más abogados) en Argentina, Uruguay, Chile, México y Colombia: 21.000" |
| ticket_anual_usd | 11.400 | mercado/legaltech-latam#2 | "Ticket anual mediano del segmento: USD 11.400" |
| porcentaje_sam_pct | 42,9 | mercado/legaltech-latam#1 | "El Cono Sur (Argentina, Uruguay y Chile) concentra 9.000 organizaciones, el 42,9 % del total" |

### Hallazgos cualitativos
- (equipo) Los fundadores trabajan a tiempo completo, tienen el 68 % de la empresa y cuentan con experiencia directa en el sector legal y en machine learning. [contralia/clientes-y-equipo#2]
- (tecnologia) El análisis de contratos depende en un 100 % de un único proveedor de LLM comercial externo. [contralia/tecnologia#4]
- (riesgo) La empresa asegura que los datos de los contratos de los clientes no se utilizan para entrenar los modelos, respondiendo a la principal barrera de adopción del sector. [contralia/tecnologia#5]

## Análisis (analista, v1)

**Costo de LLM:** USD 6.240 por mes (7,3 % del MRR).

| ARPA | Margen bruto | CAC | LTV | LTV/CAC | Payback | Runway |
|---|---|---|---|---|---|---|
| USD 950 | 71,3 % | USD 6.500 | USD 37.630 | 5,79 | 9,6 meses | 24,0 meses |

**Mercado:** TAM USD 239.400.000 · SAM USD 102.702.600 · SOM USD 5.135.130 por año. Supuesto de cuota: Captura conservadora del 5% del SAM legaltech en LATAM basándonos en la tracción actual de 90 clientes y alta retención.

**Scoring: 92,0/100 (avanzar a comité)**

| Criterio | Puntaje 0-5 | Peso | Aporte |
|---|---|---|---|
| unit_economics | 5,0 | 25 % | 25,0 |
| margen_bruto | 5,0 | 20 % | 20,0 |
| runway | 5,0 | 15 % | 15,0 |
| crecimiento | 3,0 | 15 % | 9,0 |
| equipo | 5,0 | 10 % | 10,0 |
| mercado | 4,0 | 10 % | 8,0 |
| concentracion | 5,0 | 5 % | 5,0 |

- Equipo: Los fundadores están a tiempo completo, poseen el 68% de la empresa y cuentan con experiencia directa en legaltech y machine learning.
- Mercado: Mercado grande y en crecimiento (TAM de 239M USD), con un SAM de 102.7M USD y buena tracción inicial.

**Interpretación del analista:** El análisis financiero y de unit economics para **Contralia** arroja los siguientes resultados basados en las 21 métricas registradas:

- **Costo de LLM y Margen Bruto**: El costo mensual del LLM asciende a **$6,240 USD** (un 7.3% del MRR). Esto sitúa el **margen bruto real en 71.3%**, alineándose muy de cerca con el 72% declarado por la startup tras descontar infraestructura ($6,800 USD) y otros costos directos ($11,500 USD).
- **Eficiencia Comercial**: Presenta un **ARPA de $950 USD**, un **CAC de $6,500 USD** y un robusto **LTV/CAC de 5.79x**, con un periodo de repago (**payback**) saludable de **9.6 meses**.
- **Solvencia**: Cuenta con una caja disponible de $1.15M USD y un burn neto mensual de $48,000 USD, lo que otorga un **runway de 24 meses**.
- **Scoring**: La startup obtiene un puntaje de **92/100 ("avanzar a comité")**, impulsado por sólidos márgenes, un excelente ratio LTV/CAC y un equipo fundador con dedicación y experiencia técnica y sectorial ideales.

## Red flags (crítico)

Sin red flags registradas.

## Validación

- ✅ investigacion: 21 métricas ancladas a su fuente (mínimo 6) y 3 hallazgos con cita (mínimo 2).

- ✅ metricas_clave: Todas las métricas clave están registradas.

- ✅ correcciones_investigador: Sin correcciones altas pendientes.

- ✅ analisis_vigente: Análisis v1 completo y al día.

- ✅ correcciones_analista: Sin correcciones altas pendientes.

- ✅ critica_vigente: La crítica v1 auditó el análisis v1.

## Trazabilidad: quién aportó qué

| Paso | Agente | Acción | Detalle |
|---|---|---|---|
| 1 | supervisor | → investigador | El investigador aún no entregó datos, por lo que se debe iniciar el proceso con él según la rúbrica. |
| 1 | investigador | investigación | v1: 21 métricas ancladas, 3 hallazgos, 0 registros rechazados |
| 2 | supervisor | → analista | La investigacion esta completa y sin correcciones pendientes, por lo que corresponde avanzar con el analista segun la rubrica para calcular unit economics y costos de LLM. |
| 2 | analista | análisis | v1: costo LLM USD 6.240/mes (7,3 % del MRR) · margen 71,3 % · LTV/CAC 5,79 · payback 9,6 m · runway 24,0 m · score 92,0 (avanzar a comité); 0 llamadas rechazadas por falta de respaldo |
| 3 | supervisor | → critico | El analista ya completó su trabajo y la rúbrica indica que la crítica no está vigente porque el crítico todavía no auditó el análisis [ ]. |
| 3 | critico | auditoría | v1 (auditó el análisis v1): 0 red flags (0 altas), 0 discrepancias declarado/calculado, 0 correcciones nuevas |
| 4 | supervisor | → finalizar | Todos los pasos obligatorios (investigación, análisis y crítica) se completaron con éxito y la rúbrica de suficiencia está completamente satisfecha sin puntos bloqueantes [ ]. |
| 4 | validador | validación | aprobada (intento 1, 0 advertencias) |

*Definiciones de métricas: 21 en el vocabulario de `state.py`.*
