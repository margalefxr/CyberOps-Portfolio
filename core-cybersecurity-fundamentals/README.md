# Silent Exposure · Fundamentos de Pentesting (Reconocimiento → Explotación)

**Metodología:** flujo clásico de pentest — reconocimiento, enumeración de directorios/archivos, análisis de superficie expuesta, cadena de vulnerabilidades hasta compromiso del sistema.
**Qué se hizo:** sobre una máquina de laboratorio (`lab-nublar-os`), identificación y encadenamiento de una serie de debilidades hasta lograr el compromiso completo del sistema, documentando cada fase con su evidencia.
**Resultado clave:** ninguna vulnerabilidad individual era "crítica" por sí sola — el compromiso completo fue posible por **encadenar varias debilidades menores**, el patrón más habitual en intrusiones reales frente al mito de la vulnerabilidad única y espectacular.

## Más allá del ejercicio: por qué los fundamentos siguen importando

Es tentador pensar que el reconocimiento y la enumeración manual están superados por herramientas automatizadas — pero son exactamente el criterio que un **SOC o un equipo de Threat Intel** usa para interpretar qué hace un escáner automático y detectar sus falsos negativos. Encadenar hallazgos menores hasta un compromiso total es también el patrón de ataque que un programa de **gestión de vulnerabilidades maduro (visto en `sec-vulnerability-management-assessment`)** intenta cortar antes de que ocurra, priorizando no solo por CVSS individual sino por combinaciones de exposición. Dominar el fundamento manual es lo que permite, después, confiar (o desconfiar con criterio) en la herramienta automatizada.
