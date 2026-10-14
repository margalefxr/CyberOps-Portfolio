# AxeZone · Auditoría de reconocimiento externo (OSINT / Recon pasivo)

**Rol:** Auditor de ciberseguridad · **Metodología propia:** MSA-Recon (basada en PTES, OWASP WSTG y NIST SP 800-115)
**Alcance:** Reconocimiento pasivo y de huella mínima sobre el dominio público de una cadena de locales de ocio (6 locales), sin intrusión ni explotación.

## Qué contiene

- `reports/auditoria-reconocimiento-externo.pdf` / `.html` — informe técnico completo (riesgo global, 19 hallazgos documentados con evidencia y comandos, correlación normativa RGPD/LSSI-CE/ISO 27001/ENS, diagrama de arquitectura, anexos).

## Hallazgos destacados

- DNS huérfano en un subdominio apuntando a un recurso cloud liberado (riesgo de *subdomain takeover*, CVSS 8.2).
- Cookies de seguimiento (Meta, TikTok) cargadas antes del consentimiento del usuario.
- Dependencia de dos proveedores SaaS de reservas distintos sin contrato de encargado de tratamiento (DPA) verificado, uno de ellos con transferencia internacional de datos.
- Ausencia de cabeceras de seguridad HTTP, `xmlrpc.php` accesible, versiones de CMS/plugins expuestas (con cruce contra CVE reales, confirmando o descartando cada uno por versión exacta).

## Nota sobre anonimización

Este es un trabajo **real**, realizado de forma independiente sobre un negocio real, con autorización verbal de su propietario. Para publicarlo aquí como muestra de portafolio, se han sustituido por valores ficticios: el nombre de dominio, las direcciones IP, los nombres de los proveedores externos de reservas y los nombres de local/ubicación. La metodología, los hallazgos, su severidad (CVSS) y las correcciones propuestas son fieles al trabajo original — solo se ha enmascarado lo que permitiría identificar al cliente real, conforme al RGPD y a la confidencialidad profesional habitual en este tipo de encargos.
