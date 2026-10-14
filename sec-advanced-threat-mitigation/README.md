# Black Mamba · Auditoría de Seguridad Web Corporativa

**Metodología:** MAGERIT v3 (identificación de activos, dependencias, impacto y riesgo potencial/residual) con referencia al **Esquema Nacional de Seguridad (ENS)**.
**Qué se hizo:** evaluación de la postura de seguridad de la infraestructura que soporta una web corporativa — 8 hallazgos, los más críticos ligados a versiones obsoletas de PHP, MariaDB y WordPress sin evidencia de explotación activa, pero con exposición real a vulnerabilidades conocidas.
**Resultado clave:** postura de seguridad calificada como **Deficiente** — no por un incidente confirmado, sino por la acumulación de componentes fuera de soporte sin un proceso de actualización continua, lo que por sí solo ya constituye un hallazgo de gestión de vulnerabilidades.

## Más allá del ejercicio: de hallazgo técnico a riesgo de negocio

El propio informe ya conecta el hallazgo técnico con el riesgo de negocio: interrupciones de servicio, pérdida de confianza de clientes y terceros, y la posibilidad de que un incidente sobre datos personales active obligaciones bajo el **RGPD**. Esto es, en esencia, el puente que separa a un pentester de un profesional GRC: no basta con decir "PHP 7.2 está obsoleto", hay que traducirlo a "esto nos deja fuera de la debida diligencia que exige el Art. 32 RGPD (medidas técnicas y organizativas apropiadas)" y, si la web soporta a un proveedor en la cadena de suministro de otra empresa, a la **evaluación de riesgo de terceros** que cualquier cliente corporativo debería exigir antes de integrarse con ella. Mantener software desactualizado no es solo deuda técnica — es, de cara a un auditor externo o a un cliente, una señal de madurez de seguridad insuficiente.
