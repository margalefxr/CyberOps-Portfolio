# Base de Conocimiento Técnico (Microsoft / Azure / Fundamentos)

Apuntes de referencia propia sobre fundamentos de ciberseguridad y stack Microsoft/Azure: terminología (amenaza, vulnerabilidad, exploit, riesgo, impacto, mitigación), ingeniería social, y notas operativas de administración en entornos cloud.

## Más allá de los apuntes: el modelo de responsabilidad compartida

Trabajar sobre Azure (o cualquier hyperscaler) sin tener interiorizado el **modelo de responsabilidad compartida** es el error de base más común en perfiles junior: el proveedor cloud asegura la infraestructura física y la plataforma, pero la configuración de identidad (Entra ID), el cifrado de datos, los permisos sobre recursos y la gestión de parches del sistema operativo dentro de una VM siguen siendo responsabilidad del cliente. La mayoría de incidentes cloud reales (buckets S3 públicos, roles IAM sobre-permisivos, claves en repositorios) no son fallos del proveedor — son fallos de esa frontera de responsabilidad mal entendida. Es la base sobre la que se construye después cualquier conversación de **Zero Trust** o **CSPM (Cloud Security Posture Management)**.
