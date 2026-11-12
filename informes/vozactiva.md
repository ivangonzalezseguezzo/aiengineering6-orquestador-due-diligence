# Due diligence — VozActiva

Fecha: 2026-11-11 · Decisiones del supervisor: 4 · Validación: aprobada

## Recomendación preliminar: NO AVANZAR

Motivo: score 41,0/100 (banda: no avanzar); 4 red flags de severidad alta.

> Recomendación generada por el sistema a partir de datos anclados a sus fuentes. La decisión de invertir la toma el comité con aprobación humana explícita (la PE7 agrega ese paso al flujo).

## Métricas registradas (investigador)

| Métrica | Valor | Fuente | Cita |
|---|---|---|---|
| mrr_usd | 90.000 | vozactiva/metricas#1 | "MRR recurrente (contratos mensuales): USD 90.000" |
| clientes_activos | 20 | vozactiva/metricas#2 | "Clientes con contrato recurrente: 20" |
| crecimiento_mrr_mensual_pct | 4 | vozactiva/metricas#3 | "Crecimiento mensual del MRR recurrente (últimos 6 meses): 4 %" |
| churn_mensual_pct | 6,5 | vozactiva/metricas#4 | "Churn mensual de clientes recurrentes: 6,5 %" |
| gasto_comercial_mensual_usd | 78.000 | vozactiva/finanzas#3 | "Gasto mensual en ventas y marketing: USD 78.000" |
| clientes_nuevos_mes | 2,5 | vozactiva/metricas#4 | "Clientes recurrentes nuevos por mes (promedio de los últimos 6 meses): 2,5" |
| costo_infra_mensual_usd | 9.500 | vozactiva/finanzas#1 | "Infraestructura cloud (sin incluir el LLM): USD 9.500 por mes" |
| otros_costos_directos_mensual_usd | 26.000 | vozactiva/finanzas#1 | "Otros costos directos totales (soporte más voz y telefonía): USD 26.000 por mes" |
| margen_bruto_declarado_pct | 74 | vozactiva/finanzas#2 | "Margen bruto informado: 74 %" |
| burn_neto_mensual_usd | 95.000 | vozactiva/finanzas#4 | "Burn neto mensual: USD 95.000" |
| caja_usd | 700.000 | vozactiva/finanzas#4 | "Caja disponible al 31/10/2026: USD 700.000" |
| runway_declarado_meses | 20 | vozactiva/finanzas#4 | "Runway informado: 20 meses" |
| llamadas_llm_mes | 2.400.000 | vozactiva/tecnologia#2 | "Llamadas al LLM por mes: 2.400.000" |
| tokens_entrada_por_llamada | 1.800 | vozactiva/tecnologia#2 | "Tokens de entrada promedio por llamada: 1.800" |
| tokens_salida_por_llamada | 250 | vozactiva/tecnologia#2 | "Tokens de salida promedio por llamada: 250" |
| precio_entrada_usd_millon | 2,5 | vozactiva/tecnologia#3 | "Precio por millón de tokens de entrada: USD 2,50" |
| precio_salida_usd_millon | 10 | vozactiva/tecnologia#3 | "Precio por millón de tokens de salida: USD 10" |
| clientes_potenciales_tam | 9.800 | mercado/contact-centers-latam#1 | "Centros de contacto con 50 o más posiciones en la región: 9.800" |
| porcentaje_sam_pct | 57,1 | mercado/contact-centers-latam#1 | "México, Colombia y Argentina concentran 5.600 centros, el 57,1 % del total" |
| concentracion_top_cliente_pct | 46 | vozactiva/clientes-y-equipo#1 | "El cliente más grande, TelcoAndina, representa el 46 % del MRR recurrente" |

### Hallazgos cualitativos
- (clientes) El cliente más grande, TelcoAndina, representa el 46% del MRR recurrente y su contrato vence el 31/03/2027 pidiendo un 25% de descuento. [vozactiva/clientes-y-equipo#1]
- (equipo) La CTO Lucía Benítez tiene dedicación parcial del 50% y asesora a otra empresa. [vozactiva/clientes-y-equipo#2]
- (tecnologia) Dependencia de un proveedor único de LLM sin modelo alternativo probado en producción y con aumento del 40% en tokens de entrada desde 2027. [vozactiva/tecnologia#4]
- (riesgo) El runway informado de 20 meses incluye un préstamo puente de USD 1.200.000 no firmado. [vozactiva/finanzas#4]

## Análisis (analista, v1)

**Costo de LLM:** USD 16.800 por mes (18,7 % del MRR).

| ARPA | Margen bruto | CAC | LTV | LTV/CAC | Payback | Runway |
|---|---|---|---|---|---|---|
| USD 4.500 | 41,9 % | USD 31.200 | USD 29.000 | 0,93 | 16,6 meses | 7,4 meses |

**Scoring: 41,0/100 (no avanzar)**

| Criterio | Puntaje 0-5 | Peso | Aporte |
|---|---|---|---|
| unit_economics | 2,0 | 25 % | 10,0 |
| margen_bruto | 2,0 | 20 % | 8,0 |
| runway | 2,0 | 15 % | 6,0 |
| crecimiento | 2,0 | 15 % | 6,0 |
| equipo | 2,0 | 10 % | 4,0 |
| mercado | 3,0 | 10 % | 6,0 |
| concentracion | 1,0 | 5 % | 1,0 |

- Equipo: La CTO tiene dedicación parcial (50%), lo cual es un riesgo importante para una startup de IA.
- Mercado: El mercado de contact centers en LATAM es grande, pero la competencia y la alta concentración limitan el atractivo.

**Interpretación del analista:** Como analista financiero, he procesado las métricas registradas para **VozActiva** a través de las herramientas oficiales. 

### Resumen de Resultados Financieros y Unit Economics

- **Costo de LLM:** El costo mensual asciende a **$16,800 USD**, lo que representa un **18.67%** del MRR.
- **Margen Bruto Real:** Al incorporar los costos de infraestructura, otros costos directos y el consumo real de LLM, el margen bruto real se reduce al **41.89%** (muy por debajo del 74% declarado).
- **Eficiencia Comercial:** El CAC se ubica en **$31,200 USD**, con un LTV de **$29,000 USD**, arrojando un ratio **LTV/CAC de 0.93** y un **payback de 16.6 meses**.
- **Runway:** Con una caja de $700,000 USD y un burn neto mensual de $95,000 USD, el runway real es de **7.4 meses** (el valor declarado de 20 meses contemplaba un préstamo puente no firmado).
- **Scoring de Inversión:** La startup obtiene un puntaje de **41/100**, ubicándose en la banda de **"no avanzar"**. Esto refleja unit economics débiles (LTV/CAC menor a 1), un margen bruto erosionado por los costos de IA, alta concentración de clientes (46% en un solo cliente) y un runway crítico.

## Red flags (crítico)

- **[alta] Runway artificial basado en financiamiento no firmado**: El runway real es de 7.4 meses; contar con un préstamo no firmado distorsiona la salud financiera real de la empresa. Evidencia: "Nota 5: el runway informado incluye un préstamo puente de USD 1.200.000 que está en negociación y todavía no fue firmado" [vozactiva/finanzas#4]

- **[alta] Alta concentración de clientes y riesgo de churn o descuento en cuenta principal**: Una pérdida o reducción de este cliente impactaría drásticamente la supervivencia y los ingresos de la startup. Evidencia: "El cliente más grande, TelcoAndina, representa el 46 % del MRR recurrente.
- Los 3 clientes más grandes suman el 71 % del MRR recurrente.
- El contrato con TelcoAndina vence el 31/03/2027 y está en renegociación: el cliente pide un 25 % de descuento" [vozactiva/clientes-y-equipo#1]

- **[alta] Margen bruto declarado inflado** (regla de contraste): Margen bruto declarado 74,0 % vs. calculado con todos los costos directos 41,9 % (32,1 puntos de diferencia). Evidencia: "Margen bruto informado: 74 %" [vozactiva/finanzas#2]

- **[alta] Runway declarado mayor al real** (regla de contraste): Runway declarado 20 meses vs. 7,4 meses con la caja y el burn actuales. Evidencia: "Runway informado: 20 meses" [vozactiva/finanzas#4]

## Validación

- ✅ investigacion: 20 métricas ancladas a su fuente (mínimo 6) y 4 hallazgos con cita (mínimo 2).

- ✅ metricas_clave: Todas las métricas clave están registradas.

- ✅ correcciones_investigador: Sin correcciones altas pendientes.

- ✅ analisis_vigente: Análisis v1 completo y al día.

- ✅ correcciones_analista: Sin correcciones altas pendientes.

- ✅ critica_vigente: La crítica v1 auditó el análisis v1.

## Trazabilidad: quién aportó qué

| Paso | Agente | Acción | Detalle |
|---|---|---|---|
| 1 | supervisor | → investigador | La investigacion esta vacia y la rubrica exige datos iniciales. Mandamos al investigador para registrar las metricas del data room. |
| 1 | investigador | investigación | v1: 20 métricas ancladas, 4 hallazgos, 1 registros rechazados |
| 2 | supervisor | → analista | La investigacion esta completa y aprobada, pero falta el analisis de unit economics y costos de LLM segun la rubrica. |
| 2 | analista | análisis | v1: costo LLM USD 16.800/mes (18,7 % del MRR) · margen 41,9 % · LTV/CAC 0,93 · payback 16,6 m · runway 7,4 m · score 41,0 (no avanzar); 2 llamadas rechazadas por falta de respaldo |
| 3 | supervisor | → critico | La rúbrica indica que la crítica no está vigente porque el crítico todavía no auditó el análisis v1. Debemos enviar al crítico para que audite los resultados. |
| 3 | critico | auditoría | v1 (auditó el análisis v1): 4 red flags (4 altas), 2 discrepancias declarado/calculado, 0 correcciones nuevas |
| 4 | supervisor | → finalizar | Todos los pasos obligatorios (investigación, análisis y crítica) se completaron con éxito y la rúbrica de suficiencia está totalmente satisfecha sin puntos bloqueantes [ ]. |
| 4 | validador | validación | aprobada (intento 1, 0 advertencias) |

*Definiciones de métricas: 21 en el vocabulario de `state.py`.*
