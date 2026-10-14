# TechSecure · Evaluación de Seguridad Lógica y Control de Accesos

**Metodología:** matriz de accesos, análisis de incidentes (acceso no controlado, dispositivo no autorizado conectado a la red), evaluación de riesgo por impacto × probabilidad, ciclo PDCA.
**Qué se hizo:** reconstrucción de dos incidentes de control de acceso (una cuenta con permisos excesivos, un dispositivo no gestionado conectado a la red corporativa) y propuesta de salvaguardas técnicas y de proceso.
**Resultado clave:** en ambos casos la causa raíz no es un fallo técnico puntual, sino la ausencia de un modelo de acceso basado en **mínimo privilegio** y de un proceso de **gestión de activos/NAC** que detecte dispositivos desconocidos antes de que se conecten.

## Más allá del ejercicio: de "lista de permisos" a Zero Trust

Una matriz de accesos estática es el punto de partida, pero el mercado ya no evalúa el control de acceso así: la tendencia (y lo que preguntan hoy en procesos de SOC/IAM) es **Zero Trust** — verificar continuamente identidad, dispositivo y contexto en cada petición, no solo en el login, y tratar cada dispositivo no inventariado como no confiable por defecto (**NAC — Network Access Control**). El caso del "dispositivo no autorizado conectado a la red" de este ejercicio es, en una red real, exactamente lo que detecta un sistema NAC o un EDR con descubrimiento de activos — y lo que, sin eso, se convierte en el punto de entrada favorito para moverse lateralmente hacia activos más críticos (ver el caso de segmentación en `audit-moldtek-internal-network`, donde el mismo patrón aparece con un ejemplo real).
