# Desglose de un Incidente Complejo — GlobalPay

**Auditor:** Xavier Margalef Riestra
**Actividad:** Análisis forense y de respuesta ante incidentes (DFIR) sobre una brecha de datos de tarjetas
**Fecha:** Julio 2026

---

## Contexto del incidente

GlobalPay sufre una brecha de seguridad que culmina en la exfiltración de datos de tarjetas de pago, a través de una cadena de tres fallos técnicos encadenados y un fallo organizativo de fondo. El objetivo de este análisis es doble: determinar la respuesta inmediata correcta y, para cada paso de la cadena de ataque, identificar qué auditoría preventiva lo habría detectado antes de que ocurriera.

## 1. Reacción inmediata

### ¿Qué tipo de auditoría debe ejecutarse en este momento y por qué?

La respuesta correcta es **DFIR (Digital Forensics & Incident Response)**, no una auditoría preventiva: el ataque ya se ha producido y el objetivo pasa a ser reconstruir qué ocurrió, contener el daño y preservar evidencia, no prevenir.

Las prioridades inmediatas son:

- Identificar el origen y el vector de entrada del ataque.
- Reconstruir la cadena de eventos (*timeline*) completa.
- Preservar evidencia digital (logs, memoria, discos) con cadena de custodia, antes de que se sobrescriba o se pierda.
- Establecer el alcance real de la exfiltración de datos.

En este caso concreto, DFIR es crítico por tres factores que elevan la urgencia por encima de un incidente ordinario:

- Fuga masiva de datos de tarjetas de pago.
- Impacto legal — investigación gubernamental ya en curso.
- Riesgo de pérdida de la licencia de procesamiento de pagos (Visa/Mastercard).

**Herramientas de auditoría asistida por ordenador (CAAT) aplicables en esta fase:**

| Herramienta | Función |
|---|---|
| ELK Stack / Splunk | Análisis de logs masivos y correlación de eventos |
| Wireshark | Captura y análisis de tráfico de red sospechoso |
| Autopsy | Análisis forense de discos y recuperación de evidencia |
| Snort / OSSEC | Detección de intrusiones previas al incidente actual |

## 2. Análisis de la cadena de ataque

**Pregunta de la actividad:** si GlobalPay hubiera auditado correctamente antes del ataque, ¿qué tres auditorías preventivas específicas habrían detectado y evitado cada paso de la cadena?

El marco de referencia combina gestión de proyectos IT, SDLC, seguridad de la información y ciberseguridad — cada paso técnico de la cadena tiene una auditoría preventiva específica que lo habría cortado.

### Paso 1 — XSS en portal web obsoleto → robo de sesión

**Auditoría aplicable:** seguridad en aplicaciones y APIs (OWASP), dentro del ciclo SDLC.

Qué habría detectado:
- Vulnerabilidades del OWASP Top 10 (XSS reflejado/almacenado).
- Falta de validación y sanitización de entradas de usuario.
- Ausencia de testing de seguridad integrado en el ciclo de vida del software.

Herramientas típicas: OWASP ZAP, Burp Suite, pruebas sistemáticas contra el catálogo OWASP Top 10.

### Paso 2 — Red sin segmentación: el atacante salta de soporte a bases de datos de tarjetas

**Auditoría aplicable:** auditoría de redes (*Network Security Assessment*).

Qué habría detectado:
- Falta de segmentación por VLAN entre entornos de soporte y entornos que procesan datos de tarjeta.
- Ausencia de arquitectura Zero Trust — el movimiento lateral no debería ser posible sin autenticación y autorización explícitas en cada salto.
- Movimiento lateral sin restricción entre redes críticas.

CAATs: Nmap (mapeo de red), Snort/IDS-IPS (detección de intrusiones), MITRE ATT&CK (modelado de las técnicas de movimiento lateral empleadas).

### Paso 3 — Credenciales en texto plano en un script de backup con privilegios de administrador

**Auditoría aplicable:** análisis de código (DevSecOps / *Software Security Review*).

Qué habría detectado:
- Credenciales hardcodeadas directamente en código o scripts.
- Malas prácticas de desarrollo en el manejo de secretos.
- Ausencia de revisión de código orientada a seguridad antes de desplegar.

CAATs: SAST (*Static Application Security Testing*), análisis automatizado de repositorios, scripts propios de auditoría (Python/SQL) para detectar patrones de credenciales expuestas.

### Causa raíz organizativa — gestión de proyectos IT

Los tres pasos técnicos anteriores son el *patrón* del atacante; el fallo de fondo que los habilitó a todos es distinto y no técnico: **el portal llevaba dos años sin actualizar**.

**Auditoría aplicable:** gestión de proyectos IT.

Qué habría detectado: falta de mantenimiento continuado del software, mala planificación de ciclos de actualización, y ausencia de control de calidad en los procesos de entrega. Con un proceso de mantenimiento mínimamente maduro, el sistema no habría llegado a quedar obsoleto y expuesto en primer lugar — es la auditoría que, de haberse hecho, habría evitado que los otros tres pasos fueran siquiera posibles.

## 3. Incumplimiento normativo

### ¿Qué auditoría específica reprueba la empresa en el paso 4, y a qué se enfrenta?

**Auditoría fallida:** cumplimiento normativo (*Compliance*).

**Normativas incumplidas:**
- **PCI-DSS** — estándar de seguridad para el procesamiento de datos de tarjetas de pago.
- **RGPD / LOPDGDD** — protección de datos de carácter personal.
- **ISO/IEC 27001** — gestión de la seguridad de la información.

**Consecuencias directas:** sanciones económicas significativas, apertura de investigación gubernamental, y riesgo real de pérdida de la licencia de procesamiento de pagos — este último es, en la práctica, el riesgo que puede determinar la continuidad del negocio.

> **Nota de actualidad (2026):** con **NIS2** ya transpuesta en la mayoría de estados miembros de la UE, una brecha de esta magnitud activaría además una obligación de notificación temprana en 24 horas y un informe formal en 72 horas — un plazo que corre en paralelo a la investigación forense, no después de ella. Un plan de respuesta a incidentes maduro en 2026 integra esta decisión regulatoria desde la primera hora, no la pospone hasta que termine el análisis técnico.

## 4. Priorización de la respuesta

**Planteamiento:** el CEO propone contratar urgentemente una auditoría de seguridad física para evitar que esto vuelva a ocurrir. Como auditor responsable, ¿cuál es la respuesta correcta?

La auditoría de seguridad física **no es la prioridad** ante este incidente concreto. El origen del ataque es exclusivamente lógico, y se concentra en tres planos: SDLC, segmentación de red y gestión de credenciales — ninguno de los tres se corrige con controles de acceso físico a instalaciones.

Para que la recomendación sea legible también para un perfil no técnico, cada fallo técnico tiene un equivalente directo en el mundo físico:

- El fallo de SDLC (portal publicado con XSS sin corregir) equivale a dejar la puerta de entrada de un edificio abierta y accesible desde la calle.
- La falta de segmentación de red equivale a que, una vez dentro de una sala cualquiera del edificio, se pueda acceder sin más llaves a la caja fuerte — exactamente lo que una arquitectura Zero Trust está diseñada para impedir.
- Las credenciales en texto plano equivalen a dejar la llave maestra del edificio colgada y visible en un archivo compartido al que cualquier empleado tiene acceso.

**Recomendación:** una auditoría integral de ciberseguridad basada en OWASP (SDLC), Zero Trust (arquitectura de red) y DevSecOps (gestión de secretos en código), alineada con los requisitos de PCI-DSS. La seguridad física puede incorporarse como medida complementaria dentro de ese plan, pero no es la prioridad que la situación exige ahora mismo.
