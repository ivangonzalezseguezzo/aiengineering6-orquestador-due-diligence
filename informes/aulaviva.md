# Due diligence — Aula Viva

Fecha: 2026-11-11 · Decisiones del supervisor: 5 · Validación: aprobada

## Recomendación preliminar: SIN RECOMENDACIÓN

Motivo: información insuficiente: faltan 13 métricas clave (crecimiento_mrr_mensual_pct, churn_mensual_pct, concentracion_top_cliente_pct, gasto_comercial_mensual_usd, clientes_nuevos_mes, costo_infra_mensual_usd, otros_costos_directos_mensual_usd, burn_neto_mensual_usd, llamadas_llm_mes, tokens_entrada_por_llamada, tokens_salida_por_llamada, precio_entrada_usd_millon, precio_salida_usd_millon); pedirlas a la startup.

> Recomendación generada por el sistema a partir de datos anclados a sus fuentes. La decisión de invertir la toma el comité con aprobación humana explícita (la PE7 agrega ese paso al flujo).

## Métricas registradas (investigador)

| Métrica | Valor | Fuente | Cita |
|---|---|---|---|
| mrr_usd | 6.200 | aulaviva/pitch#3 | "MRR de USD 6.200" |
| clientes_activos | 11 | aulaviva/carta-inversores#2 | "Colegios que pagan una suscripción: 11" |
| caja_usd | 150.000 | aulaviva/carta-inversores#3 | "Caja disponible: USD 150.000" |
| clientes_potenciales_tam | 38.000 | mercado/edtech-latam#1 | "Colegios secundarios privados en la región: 38.000" |
| porcentaje_sam_pct | 12,1 | mercado/edtech-latam#1 | "Argentina tiene 4.600 colegios secundarios privados, el 12,1 % del total regional" |

**No disponibles en las fuentes:** crecimiento_mrr_mensual_pct, churn_mensual_pct, concentracion_top_cliente_pct, gasto_comercial_mensual_usd, clientes_nuevos_mes, costo_infra_mensual_usd, otros_costos_directos_mensual_usd, burn_neto_mensual_usd, llamadas_llm_mes, tokens_entrada_por_llamada, tokens_salida_por_llamada, precio_entrada_usd_millon, precio_salida_usd_millon.

### Hallazgos cualitativos
- (equipo) Los fundadores son tres y solo dos trabajan a tiempo completo en la startup. [aulaviva/carta-inversores#4]
- (riesgo) Los costos de IA están cubiertos por créditos promocionales hasta marzo de 2027. [aulaviva/carta-inversores#3]
- (clientes) La mayoría de los colegios usa un piloto gratuito de tres meses y todavía no miden churn. [aulaviva/carta-inversores#2]

## Análisis (analista, v1)

| ARPA | Margen bruto | CAC | LTV | LTV/CAC | Payback | Runway |
|---|---|---|---|---|---|---|
| USD 564 | s/d | s/d | s/d | s/d | s/d meses | s/d meses |

- No calculable: margen_bruto_pct (faltan los costos directos)

- No calculable: cac_usd (faltan gasto_comercial_mensual_usd o clientes_nuevos_mes)

- No calculable: ltv_usd (faltan ARPA, margen bruto o churn_mensual_pct)

- No calculable: payback_meses (faltan el CAC o el margen por cliente)

- No calculable: runway_meses (faltan caja_usd o burn_neto_mensual_usd)

**Scoring: 12,0/100 (no avanzar)**

| Criterio | Puntaje 0-5 | Peso | Aporte |
|---|---|---|---|
| unit_economics | 0,0 | 25 % | 0,0 |
| margen_bruto | 0,0 | 20 % | 0,0 |
| runway | 0,0 | 15 % | 0,0 |
| crecimiento | 0,0 | 15 % | 0,0 |
| equipo | 3,0 | 10 % | 6,0 |
| mercado | 3,0 | 10 % | 6,0 |
| concentracion | 0,0 | 5 % | 0,0 |

Criterios sin dato (suman 0): ltv_cac, payback_meses, margen_bruto_pct, runway_meses, crecimiento_mrr_mensual_pct, concentracion_top_cliente_pct.

- Equipo: Tres fundadores pero solo dos dedicados a tiempo completo, lo que reduce ligeramente la puntuación.
- Mercado: Mercado edtech con TAM definido, pero la falta de métricas avanzadas limita la visibilidad.

**Interpretación del analista:** Con base en las métricas registradas, los cálculos y las herramientas financieras, presento el resumen del análisis para Aula Viva:

- **Margen real y Unit Economics:** El ARPA es de $563.64 USD por cliente activo. No fue posible calcular el margen bruto real, el CAC, el LTV, el payback ni el runway debido a la ausencia de datos sobre costos directos, gasto comercial, churn y burn rate neto. Los costos de IA están cubiertos por créditos promocionales hasta marzo de 2027.
- **Eficiencia comercial:** Indeterminada por falta de métricas de gasto comercial, clientes nuevos y churn mensual.
- **Runway:** No calculable por no contar con el dato de burn rate mensual (aunque se dispone de $150,000 USD en caja).
- **Scoring:** La startup obtuvo un puntaje total de 12/100, clasificándose en la banda "no avanzar", fuertemente penalizada por la falta de métricas clave operativas y financieras en el data room.

## Red flags (crítico)

- **[alta] Dependencia de créditos promocionales para cubrir costos de IA**: Los costos de IA están enmascarados por créditos promocionales temporales, lo que distorsiona el margen bruto real que tendrá la empresa al vencer dichos créditos. Evidencia: "El costo de IA lo cubren créditos promocionales del proveedor hasta marzo de 2027" [aulaviva/carta-inversores#3]

## Validación

- ⚠️ investigacion: 5 métricas ancladas a su fuente (mínimo 6) y 3 hallazgos con cita (mínimo 2). (sin más intentos: queda como salvedad)

- ⚠️ metricas_clave: No disponibles en las fuentes tras 2 búsquedas: crecimiento_mrr_mensual_pct, churn_mensual_pct, concentracion_top_cliente_pct, gasto_comercial_mensual_usd, clientes_nuevos_mes, costo_infra_mensual_usd, otros_costos_directos_mensual_usd, burn_neto_mensual_usd, llamadas_llm_mes, tokens_entrada_por_llamada, tokens_salida_por_llamada, precio_entrada_usd_millon, precio_salida_usd_millon.

- ✅ correcciones_investigador: Sin correcciones altas pendientes.

- ✅ analisis_vigente: Análisis v1 completo y al día.

- ✅ correcciones_analista: Sin correcciones altas pendientes.

- ✅ critica_vigente: La crítica v1 auditó el análisis v1.

## Trazabilidad: quién aportó qué

| Paso | Agente | Acción | Detalle |
|---|---|---|---|
| 1 | supervisor | → investigador | El proceso recién empieza y la rúbrica muestra que el investigador todavía no entregó datos, por lo que es necesario asignarle la primera tarea. |
| 1 | investigador | investigación | v1: 3 métricas ancladas, 3 hallazgos, 1 registros rechazados; faltan crecimiento_mrr_mensual_pct, churn_mensual_pct, concentracion_top_cliente_pct, gasto_comercial_mensual_usd, clientes_nuevos_mes, costo_infra_mensual_usd, otros_costos_directos_mensual_usd, burn_neto_mensual_usd, llamadas_llm_mes, tokens_entrada_por_llamada, tokens_salida_por_llamada, precio_entrada_usd_millon, precio_salida_usd_millon |
| 2 | supervisor | → investigador | Faltan métricas clave y llegar al mínimo de 6 requeridas por la rúbrica, por lo que debo enviar nuevamente al investigador a completarlas. |
| 2 | investigador | investigación | v2: 5 métricas ancladas, 3 hallazgos, 1 registros rechazados; faltan crecimiento_mrr_mensual_pct, churn_mensual_pct, concentracion_top_cliente_pct, gasto_comercial_mensual_usd, clientes_nuevos_mes, costo_infra_mensual_usd, otros_costos_directos_mensual_usd, burn_neto_mensual_usd, llamadas_llm_mes, tokens_entrada_por_llamada, tokens_salida_por_llamada, precio_entrada_usd_millon, precio_salida_usd_millon |
| 3 | supervisor | → analista | El investigador ya agotó o avanzó suficiente y la rúbrica indica que falta el análisis. Como el analista todavía no calculó (punto [x] bloqueante en analisis_vigente), corresponde enviarle la tarea. |
| 3 | analista | análisis | v1: margen s/d · LTV/CAC s/d · payback s/d m · runway s/d m · score 12,0 (no avanzar); 1 llamadas rechazadas por falta de respaldo |
| 4 | supervisor | → critico | El analista ya procesó los datos, pero el crítico todavía no auditó el análisis (punto [ ] en la rúbrica). Debemos enviar al crítico. |
| 4 | critico | auditoría | v1 (auditó el análisis v1): 1 red flags (1 altas), 0 discrepancias declarado/calculado, 0 correcciones nuevas |
| 5 | supervisor | → finalizar | El investigador agotó sus intentos (2/3 pero con 2 búsquedas fallidas registradas en rúbrica) y la investigación tiene una salvedad [!] aceptable. El análisis y la crítica están vigentes y no hay correcciones pendientes, por lo que podemos finalizar el proceso. |
| 5 | validador | validación | aprobada (intento 1, 2 advertencias) |

*Definiciones de métricas: 21 en el vocabulario de `state.py`.*
