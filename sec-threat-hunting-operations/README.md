# Análisis de Riesgo Operacional · Propagación de Impacto y BCP

**Metodología:** cuantificación de impacto en cadena de dependencias (MAGERIT v3), aplicación de salvaguardas con eficacia parcial sobre nodos intermedios, principios de **Business Continuity Planning (ISO 22301)**.
**Qué se hizo:** modelado de la propagación de una degradación desde un componente base (Servidor D) hacia dos nodos intermedios en paralelo (B y C) y su convergencia final sobre el activo crítico superior (Sistema A), con y sin salvaguardas.
**Resultado clave:** la eficacia de una salvaguarda se calcula sobre el impacto parcial ya recibido por el nodo, no restando directamente del daño original — un matiz metodológico que cambia el resultado final y que suele ser el error más común al estimar riesgo residual.

## Más allá del ejercicio: de la hoja de cálculo al mapa de detección

Este mismo ejercicio de propagación de impacto es, en un SOC real, la base para decidir **dónde instrumentar detección primero**. Si un atacante compromete el nodo base (Servidor D), las técnicas de MITRE ATT&CK relevantes (movimiento lateral, escalada hacia los nodos B/C) son exactamente los puntos donde un programa de **Threat Hunting** maduro coloca sus hipótesis de caza: no se cazan amenazas al azar, se cazan donde el análisis de impacto dice que una intrusión haría más daño. Unir BCP/MAGERIT con Threat Hunting —en lugar de tratarlos como disciplinas separadas— es la diferencia entre un SOC reactivo y uno que prioriza su tiempo de detección según el impacto real de negocio, no según el volumen de alertas.
