# El Contenedor Desconocido · Respuesta a Incidente en Docker

**Metodología:** triage de contenedores (`docker ps`, inspección de imagen, logs), diferenciación entre activos autorizados y no autorizados, contención del contenedor sospechoso.
**Qué se hizo:** sobre un servidor Ubuntu con un servicio web corporativo en Docker, identificación de un segundo contenedor (`worker-17`) no documentado ni autorizado, ejecutando junto al servicio legítimo (`web-corporativa`) — análisis de su imagen, comportamiento y contención.
**Resultado clave:** el contenedor sospechoso no estaba explotando nada del servicio web — estaba ahí porque **nadie controlaba qué se desplegaba en ese host**, que es un problema de gobierno de la plataforma, no un ataque sofisticado.

## Más allá del ejercicio: supply chain de contenedores, no solo "incidente raro"

Un contenedor no autorizado en un host de producción es el ejemplo de manual de **riesgo de cadena de suministro de software** aplicado a contenedores: ¿de dónde viene la imagen?, ¿tiene procedencia verificada (firma/SLSA), o pudo entrar por un pipeline CI/CD sin control de qué imágenes se permite desplegar? La industria responde a esto con **escaneo de imágenes antes de desplegar, políticas de admisión (admission controllers) que bloquean imágenes no firmadas, y un registro privado como única fuente permitida** — en lugar de descubrir el contenedor sospechoso a posteriori con `docker ps`, como en este ejercicio. La guía de referencia aquí es la de **CISA/NSA sobre seguridad de Kubernetes/contenedores**: "detectar lo inesperado" está bien como respuesta a incidente, pero el objetivo de un programa maduro es que lo inesperado nunca llegue a ejecutarse.
