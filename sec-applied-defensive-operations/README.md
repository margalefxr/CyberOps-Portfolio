# Demuestra tus Habilidades · Evaluación de Riesgos Multisector

**Metodología:** clasificación de incidentes (ciberseguridad vs. seguridad de la información), evaluación de riesgo (impacto × probabilidad), salvaguardas técnicas/administrativas, ciclo PDCA — aplicado a tres escenarios sectoriales distintos: ransomware en un hospital, filtración de datos en una tecnológica, fallo de un PLC en una planta industrial.
**Qué se hizo:** para cada escenario, diagnóstico de la vulnerabilidad real (no solo el ataque), clasificación correcta (un fallo de política de datos ≠ un ataque técnico, aunque el resultado final sea el mismo: información comprometida) y plan de salvaguardas con su ciclo PDCA.
**Resultado clave:** el caso de la planta industrial no es un problema de "parcheo lento" — es la falta de un proceso de **gestión de vulnerabilidades sobre OT/ICS**, un dominio con reglas distintas a IT porque parar para parchear puede parar la producción.

## Más allá del ejercicio: por qué cada sector tiene su propia normativa

Estos tres escenarios no son intercambiables a nivel regulatorio, y tratarlos igual sería un error de un analista junior:
- **Sanidad (hospital):** sector crítico bajo **NIS2**, con el agravante de que el RGPD trata los datos de salud como categoría especial (Art. 9) — una brecha aquí no es "solo" una multa, es una obligación reforzada de notificación.
- **Industria (ICS/OT, planta industrial):** aquí la referencia no es ISO 27001 sino **IEC 62443**, el estándar específico para seguridad de sistemas de control industrial, porque un PLC sin parchear no se gestiona con el mismo SLA que un servidor de oficina — primero hay que entender el proceso físico que controla.
- **Tecnológica (filtración de datos):** el caso de libro de **gobierno de la seguridad de la información** sin incidente técnico de por medio — exactamente el tipo de hallazgo que una auditoría ISO 27001 (dominio de políticas, A.5) detecta antes de que se convierta en incidente.

Saber qué marco normativo aplica a cada sector —y no solo saber "arreglar la vulnerabilidad"— es la diferencia entre ejecutar un checklist y hacer GRC de verdad.
