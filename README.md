# 🛡️ Road to Cybersecurity

Documentación técnica y resolución de laboratorios prácticos — y, a partir de aquí, también casos de auditoría real llevados de forma independiente.

## 🔍 Casos de auditoría real

A diferencia del resto del repositorio (laboratorios, retos y ejercicios formativos — ver más abajo), las siguientes carpetas documentan **trabajo de campo real**: auditorías sobre infraestructura de terceros, con autorización expresa del responsable en cada caso, realizadas en el marco de mi actividad profesional actual — una combinación de colaboraciones independientes (freelance) y mi colaboración part-time con Section9, una consultora de ciberseguridad especializada en auditorías para pequeñas y medianas empresas.

| Caso | Tipo | Resumen |
|---|---|---|
| [`audit-axezone-external-recon`](./audit-axezone-external-recon) | Reconocimiento externo (OSINT / recon pasivo) | Auditoría de huella digital externa de una cadena de locales: 19 hallazgos, desde un DNS huérfano con riesgo de *subdomain takeover* hasta dependencias de terceros sin DPA verificado. Metodología propia (MSA-Recon). |
| [`audit-moldtek-internal-network`](./audit-moldtek-internal-network) | Reconocimiento de red interna | Auditoría no intrusiva de una red corporativa `/24` (92 hosts): segmentación deficiente de infraestructura crítica, credenciales en claro, CVE sin parchear. Metodología propia (MSA-Interno), con informe técnico y resumen ejecutivo de una página. |

**Confidencialidad:** en ambos casos, los datos que permitirían identificar al cliente real (dominio, direcciones IP públicas, nombres de proveedores, nombres de empleados) han sido sustituidos por valores ficticios antes de publicarse, conforme al RGPD y a la práctica profesional habitual de confidencialidad con el cliente. La metodología, los hallazgos, su severidad (CVSS/CWE) y las correcciones propuestas son fieles al trabajo original — solo se enmascara lo que identificaría a un tercero. Cada carpeta detalla en su propio README qué se anonimizó y por qué.

## 📚 Laboratorios y ejercicios formativos

El resto del repositorio recoge prácticas, retos (TryHackMe, MAGERIT, etc.) y documentación de aprendizaje realizados durante mi formación — material de entrenamiento, no auditorías sobre infraestructura real:

- `audit-shopcloud-cloud-assessment`, `audit-fortune-bank-compliance` — ejercicios de auditoría sobre escenarios de laboratorio.
- `sec-*`, `secops-*`, `core-*` — prácticas por área (hardening, threat hunting, forense/IR, monitorización SOC, gobierno de la seguridad, fundamentos).
- `automation-bash-scripting`, `knowledge-base-engineering` — automatización y apuntes técnicos.
- `profile-career-roadmap` — plan de carrera.
