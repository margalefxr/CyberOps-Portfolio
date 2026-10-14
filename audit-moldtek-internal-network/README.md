# MoldTek Industrial · Auditoría de seguridad de red interna

**Rol:** Auditor de ciberseguridad · **Metodología propia:** MSA-Interno (adaptación de MSA-Recon a reconocimiento de red interna, MI1–MI6)
**Alcance:** Reconocimiento interno no intrusivo de una red corporativa `/24` (92 hosts activos confirmados), sin explotación, sin captura de credenciales y sin pruebas de acceso de ningún tipo.

## Qué contiene

- `reports/auditoria-seguridad-red-interna.pdf` / `.html` — informe técnico completo (riesgo global, 7 hallazgos MAT-01 a MAT-07 con evidencia y comandos, correlación MITRE ATT&CK, ISO 27001/ENS/NIS2/CIS Controls v8, topología de red, decisiones y límites de alcance).
- `reports/resumen-ejecutivo-1pagina.pdf` / `.html` — resumen ejecutivo de una página para dirección, con severidad en semáforo, CVE/CWE, impacto legal/económico/operativo y correcciones.

## Hallazgos destacados

- Credenciales de administración de un dispositivo transmitidas en texto claro por HTTP.
- Infraestructura crítica (gestión remota de servidores, hipervisores, NAS) sin segmentar de los puestos de usuario — el hallazgo con más impacto estructural del informe.
- Interfaz de administración remota del Controlador de Dominio accesible desde toda la red de usuarios (mitigado parcialmente por NLA, verificado en el propio ejercicio).
- Servidor con una CVE real conocida (CVSS 6.3) sin parchear desde hace más de un año.

## Nota sobre anonimización

Este es un trabajo **real**, realizado de forma independiente sobre la red de una empresa real, con autorización del responsable del ejercicio. Para publicarlo aquí como muestra de portafolio, se ha sustituido el nombre de la empresa y los nombres de usuario/equipo del personal (datos de carácter personal bajo RGPD) por valores ficticios. Las direcciones IP mostradas son privadas (RFC 1918, `192.168.1.0/24`) y no identifican por sí solas ninguna organización, por lo que se han mantenido sin modificar. La metodología, los hallazgos, su severidad y las correcciones propuestas son fieles al trabajo original.
