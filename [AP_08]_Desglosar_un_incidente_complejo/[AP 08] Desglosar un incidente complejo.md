# [AP 08] Desglosa un incidente complejo

## Portada

Nombre: Xavier Margalef Riestra

Actividad: [AP 08] Desglosar un incidente complejo

Fecha entrega: 14 de Julio 20226



## Actividades

### Reacción Inmediata

#### ¿Qué tipo de auditoría debe ejecutarse en este mismo momento y por qué?

Respuesta a Incidentes dentro de Seguridad de la Información y Ciberseguridad

Habria que relizar un **DFIR**, ya que entra en acción después de que se ha producido un incidente o ciberataque y en esta ocasion el ataque ya ha sido perpretado y ha habido consecuencs por lo que tenemos que identificar y recopiar informacion sobre que ha pasado y como reaccionar:

- Identificar el origen del ataque
- Reconstruir la cadena de eventos (timeline)
- Preservar evidencias digitales (logs, memoria, discos)
- Establecer el alcance real de la exfiltración de datos

En este caso concreto, **DFIR** es crítica porque hay:

- fuga masiva de datos
- impacto legal (investigación gobierno)
- riesgo de pérdida de licencias (Visa/Mastercard)
  
**CAATs** utilizados en esta fase:
- ELK Stack / Splunk → análisis de logs masivos
- Wireshark → tráfico de red sospechoso
- Autopsy → análisis forense de discos
- Snort / OSSEC → detección de intrusiones previas




## Análisis

*Si GlobalPay hubiera hecho bien su trabajo antes del ataque, ¿qué TRES tipos específicos de auditorías preventivas habrían detectado y evitado los pasos 1, 2 y 3 del atacante? Relaciona cada auditoría con su paso correspondiente.*

Aqui aplicamos gestión de proyectos IT + SDLC + Seguridad de la información + Ciberseguridad

#### PASO 1: XSS en portal web obsoleto → robo de sesión

Utilizamos **Aplicaciones y desarrollo (SDLC). Análisis web (Seguridad en Aplicaciones y APIs / OWASP)**

Habría detectado:
    vulnerabilidades OWASP Top 10 (XSS)
    falta de validación de entradas
    ausencia de testing en ciclo de vida del software
Herramientas típicas:
    OWASP ZAP
    Burp Suite
    pruebas basadas en OWASP Top 10

### PASO 2 — Red sin segmentación, el atacante salta de soporte → bases de datos de tarjetas

Utilizariamos **Seguridad de la información y ciberseguridad. Auditoría de redes (Network Security Assessment)**

Qué habría detectado:
    falta de segmentación VLAN
    ausencia de arquitectura Zero Trust
    movimiento lateral libre entre redes críticas
CAATs:
    Nmap → mapeo de red
    Snort / IDS-IPS → detección de intrusiones
    MITRE ATT&CK → modelado de técnicas de ataque

### PASO 3 — Credenciales en texto plano. Script de backup con contraseña de administrador expuesta

Utilizariamos **Aplicaciones y desarrollo (SDLC). Análisis de código (DevSecOps / Software Security)**.

Qué habría detectado:
    credenciales hardcodeadas
    malas prácticas de programación
    falta de revisión de código
CAATs:
    SAST (Static Application Security Testing)
    análisis de repositorios de código
    scripts de auditoría (Python/SQL)

### GESTIÓN DE PROYECTOS IT (**fallo estructural**) causa raiz organizativa que no forma parte del patron del atacante
Problema:
Portal sin actualizar durante 2 años
**Auditoría: Gestión de proyectos IT**
Qué habría detectado:
    falta de mantenimiento del software
    mala planificación de actualizaciones
    ausencia de control de calidad en entregas
Resultado: el sistema no habría quedado obsoleto

## Normativa

### ¿Qué auditoría específica acaba de reprobar estrepitosamente la empresa en el paso 4, enfrentándose a multas millonarias?

Auditoría fallida: **Auditoría de cumplimiento normativo (Compliance)**
Normativas incumplidas:
    PCI-DSS (tarjetas de crédito)
    RGPD / LOPD (datos personales)
    ISO 27001 (seguridad de la información)
Consecuencias:
    multas económicas elevadas
    investigación gubernamental
    pérdida de licencia de procesamiento de pagos


## Reacciones

*El Director General (CEO) propone contratar urgentemente una Auditoría de Seguridad Física para evitar que esto vuelva a pasar. Como Auditor Jefe, ¿qué le responderías?*

La auditoría de seguridad física no es prioritaria en este incidente. El origen del ataque es exclusivamente lógico y se encuentra en fallos de SDLC, segmentación de red y gestión de credenciales.
Por ejemplo, el fallo de SDLC se ve cuando una web se publica con vulnerabilidades como XSS (OWASP), como si se dejara una “puerta abierta” en una aplicación accesible desde Internet.
La falta de segmentación de red permite que, una vez dentro del sistema de soporte, el atacante acceda a bases de datos críticas, como si todas las salas de un edificio pudieran abrirse sin llaves (principio que Zero Trust evitaría).
La mala gestión de credenciales ocurre al almacenar contraseñas en texto plano, equivalente a dejar una llave de acceso general visible en un archivo compartido.
La respuesta correcta es una auditoría integral de ciberseguridad basada en OWASP, Zero Trust, DevSecOps y PCI-DSS. La seguridad física solo sería complementaria.