# Informe de Evaluación de Riesgos: Seis Escenarios de Incidente

**Auditor:** Xavier Margalef Riestra · **Fecha:** 2026-06-01
**Metodología:** Clasificación de salvaguardas (Técnica/Administrativa/Física) · Ciclo PDCA · Riesgo = Impacto × Probabilidad

## Resumen

Evaluación de seis escenarios de incidente de naturaleza distinta — ransomware hospitalario, filtración de datos por error humano, fallo en un sistema industrial, acceso no autorizado a un servidor bancario, robo de equipos y fraude por ingeniería social — aplicando en cada caso el mismo marco de análisis: amenaza y vulnerabilidad explotada, salvaguarda más efectiva por tipo (técnica/administrativa/física), fase del ciclo PDCA que activa, clasificación del incidente (seguridad de la información, ciberseguridad o seguridad física) y riesgo = impacto × probabilidad.

## 1. Ataque ransomware en un hospital

| | |
|---|---|
| **Amenaza** | Ransomware |
| **Vulnerabilidad** | Ausencia de copias de seguridad recientes, sin segmentación de red ni aislamiento por virtualización que frene la propagación lateral |
| **Salvaguarda técnica** | Backups periódicos automatizados (crontab) + EDR/antivirus actualizados |
| **Salvaguarda administrativa** | Política de backup formal |
| **Salvaguarda física** | Control de acceso a hardware, por si la infección entró por ese vector (no especificado en el enunciado) |
| **PDCA** | *Plan* — define estrategia de continuidad y políticas de backup. *Act* — postmortem: recuperar datos, limpiar el sistema, implementar las salvaguardas e iniciar un nuevo ciclo |
| **Clasificación** | **Ciberseguridad** — el ransomware venció las defensas existentes — con impacto directo en **Seguridad de la Información**: confidencialidad y disponibilidad de historiales clínicos |
| **Riesgo** | **Crítico** · Impacto *muy alto* (interrupción de atención médica, pérdida de datos de salud con protección de derechos fundamentales, daño reputacional) · Probabilidad *alta* (los hospitales son objetivo frecuente por sistemas desactualizados y la urgencia de recuperar datos críticos para la vida) |

## 2. Filtración de datos en una empresa tecnológica

| | |
|---|---|
| **Amenaza** | Envío accidental de datos sensibles por error humano — [insider threat](https://www.microsoft.com/en-gb/security/business/security-101/what-is-insider-threat) involuntario |
| **Vulnerabilidad** | Falta de política de gestión de permisos y sin control/revisión automática de la salida de datos por canales profesionales |
| **Salvaguarda administrativa** | Control de acceso por rol (modelo tipo Bell-LaPadula) + formación continua en seguridad de la información |
| **Salvaguarda técnica** | Monitorización, bloqueo y alerta de envío de datos sensibles (DLP) |
| **Salvaguarda física** | No aplica |
| **PDCA** | *Plan* — procedimientos y políticas de acceso. *Check* — auditoría continua con la herramienta DLP. *Act* — hardening con lo aprendido |
| **Clasificación** | **Seguridad de la Información** — no hay un ataque que venza una defensa técnica; es la política la que tenía un hueco no previsto, no un fallo de herramienta |
| **Riesgo** | **Crítico** · Impacto *alto* (pérdida de confidencialidad de clientes, sanciones, daño reputacional) · Probabilidad *alta* (el error humano sigue siendo la causa predominante en incidentes de seguridad de la información — paralelismo real: el envío accidental de una película completa por un empleado de un estudio de animación, filtrada después en redes) |

## 3. Fallo en un sistema crítico de una planta industrial

| | |
|---|---|
| **Amenaza** | Fallo operacional en el ICS por software de control vulnerable y sin parchear, que expone los PLC a manipulación |
| **Vulnerabilidad** | Bug conocido sin parchear, sin proceso de revisión de CVE públicos |
| **Salvaguarda técnica** | Parcheo de vulnerabilidades conocidas + testing/QA antes de desplegar cambios |
| **Salvaguarda administrativa** | Política de ciberseguridad con calendario de mantenimiento preventivo |
| **Salvaguarda física** | Control de acceso físico a los equipos de control industrial |
| **PDCA** | *Plan* — calendario de mantenimiento y gestión de vulnerabilidades. *Check* — monitorización de errores/accesos y auditoría. *Act* — corregir el bug y retroalimentar la mejora |
| **Clasificación** | **Ciberseguridad Industrial** |
| **Riesgo** | **Crítico** · Impacto *alto* (pérdidas económicas y parada total de producción) · Probabilidad *alta* (entornos OT/IoT con hardware desfasado y vulnerabilidades sin parchear por años) |

## 4. Acceso no autorizado a un servidor bancario

| | |
|---|---|
| **Amenaza** | Atacante externo con credenciales extraídas de la dark web |
| **Vulnerabilidad** | Servidor sin autenticación fuerte ni MFA, reutilización de credenciales filtradas, sin SIEM que detecte accesos anómalos |
| **Salvaguarda técnica** | MFA/2FA, hardening del servidor, mejora de IAM, SIEM |
| **Salvaguarda administrativa** | Política de contraseñas (rotación, formato mínimo) + formación |
| **Salvaguarda física** | No aplica — el vector fue de red, no acceso presencial |
| **PDCA** | *Plan* — políticas de acceso, contraseñas y formación. *Do* — reset de contraseñas, activar MFA, hardening. *Check* — auditoría periódica de accesos y configuración. *Act* — postmortem |
| **Clasificación** | **Ciberseguridad** (el ataque venció las defensas existentes) + **Seguridad de la Información** (faltaban políticas de base) |
| **Riesgo** | **Crítico** · Impacto *muy alto* (exposición de datos bancarios, operaciones fraudulentas, multas regulatorias, daño reputacional) · Probabilidad *alta* (las credenciales filtradas son un vector común en banca; bots exploran continuamente este tipo de vulnerabilidad) |

## 5. Robo de equipos con información sensible

| | |
|---|---|
| **Amenaza** | Robo físico de dispositivos con datos sin cifrar |
| **Vulnerabilidad** | Sin cifrado de disco en los portátiles, sin control de acceso físico ni monitorización de instalaciones, sin MDM para borrado remoto |
| **Salvaguarda física** | La más crítica aquí — es la que habilita el resto: control de acceso, cámaras, cerraduras, vigilancia |
| **Salvaguarda técnica** | Cifrado de disco + [MDM](https://www.ibm.com/es-es/think/topics/mobile-device-management) |
| **Salvaguarda administrativa** | Política de seguridad física y respuesta ante robo |
| **PDCA** | *Plan* — seguridad de perímetro, acceso biométrico, despliegue de MDM. *Act* — postmortem y retroalimentación a Plan |
| **Clasificación** | **Seguridad de la Información + Seguridad Física** — no se vence ninguna medida de ciberseguridad porque no existía la estrategia de arquitectura que las sustentara |
| **Riesgo** | **Alto** · Impacto *alto* (pérdida de confidencialidad, riesgo de alteración, uso fraudulento) · Probabilidad *media* (la falta simultánea de protección física y digital es menos común hoy, y el acceso físico expone al atacante) |

## 6. Fraude por ingeniería social

| | |
|---|---|
| **Amenaza** | Fraude mediante phishing / ingeniería social |
| **Vulnerabilidad** | Sin política de verificación para acciones financieras ni formación — el empleado no tenía claro que debía reportar la duda |
| **Salvaguarda administrativa** | Política de verificación de pagos por doble canal + formación en detección de phishing |
| **Salvaguarda técnica** | Filtros antiphishing y alertas de correo |
| **Salvaguarda física** | No aplica |
| **PDCA** | *Plan* — políticas de verificación y formación. *Do* — desplegar filtros y sesiones de formación. *Check* — auditar transacciones y cumplimiento. *Act* — analizar causa y mejorar |
| **Clasificación** | **Seguridad de la Información** — no se compromete infraestructura; la vulnerabilidad fue de previsión técnica y formativa |
| **Riesgo** | **Crítico** · Impacto *alto* (desvío de 100.000 €, equivalente a un SEV1 por su magnitud, más riesgo legal y reputacional) · Probabilidad *alta* (el error humano explica más del 90% de las vulneraciones de seguridad de la información, y el phishing es el vector más barato y accesible) |
