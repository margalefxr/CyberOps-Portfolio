<div align="center">

# 🛡️ Xavier Margalef — CyberOps Portfolio

**SOC Analyst · Security Operations · Vulnerability Management**
Técnico de soporte L3/SRE con casi 6 años de experiencia en entornos de producción, especializado ahora en ciberseguridad defensiva y ofensiva.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/xaviermargaleftech/)
[![Email](https://img.shields.io/badge/Email-margalef.xr%40gmail.com-333?style=flat&logo=gmail&logoColor=white)](mailto:margalef.xr@gmail.com)
![CompTIA Security+](https://img.shields.io/badge/CompTIA%20Security%2B-In%20Progress-informational)
![MS SC-200](https://img.shields.io/badge/MS%20SC--200-In%20Progress-informational)
![Location](https://img.shields.io/badge/Barcelona-Spain-lightgrey)

</div>

---

## 🧭 Sobre este repositorio

Este portafolio reúne dos tipos de contenido, claramente separados para que se entienda de un vistazo qué es cada cosa:

1. **Auditorías reales** — trabajo de campo sobre infraestructura de terceros, con autorización expresa, realizado en el marco de mi actividad profesional actual (colaboraciones independientes + mi colaboración part-time con **Section9**, consultora de ciberseguridad especializada en auditorías para pymes).
2. **Laboratorios y ejercicios formativos** — prácticas, retos (TryHackMe, escenarios MAGERIT/ENS) y documentación técnica de mi formación en ciberseguridad.

Metodología común a ambos: identificación de activos → análisis de riesgo (MAGERIT v3 / ENS) → hallazgos trazables a evidencia → corrección priorizada por impacto, alineado con ISO/IEC 27001, NIST SP 800-115, MITRE ATT&CK, CIS Controls v8 y, cuando aplica, RGPD/NIS2.

---

## 🔍 Auditorías reales

| Proyecto | Tipo | Resumen |
|---|---|---|
| [`audit-axezone-external-recon`](./audit-axezone-external-recon) | Reconocimiento externo (OSINT / recon pasivo) | Huella digital externa de una cadena de locales: 19 hallazgos, desde un DNS huérfano con riesgo de *subdomain takeover* (CVSS 8.2) hasta dependencias de terceros sin DPA verificado. Metodología propia **MSA-Recon**, correlación RGPD/LSSI-CE/ISO 27001/ENS. |
| [`audit-moldtek-internal-network`](./audit-moldtek-internal-network) | Reconocimiento de red interna | Red corporativa `/24` (92 hosts activos): segmentación deficiente de infraestructura crítica, credenciales en claro, CVE sin parchear. Metodología propia **MSA-Interno**, correlación MITRE ATT&CK/ISO 27001/NIS2/CIS Controls v8. Incluye informe técnico + resumen ejecutivo de una página. |

> **Confidencialidad:** los datos que permitirían identificar al cliente real (dominio, IPs públicas, proveedores, nombres de empleados) se sustituyeron por valores ficticios antes de publicarse, conforme al RGPD y a la confidencialidad profesional habitual. Metodología, hallazgos, severidad (CVSS/CWE) y correcciones son fieles al trabajo original. Cada carpeta detalla en su README qué se anonimizó.

---

## 📚 Laboratorios y ejercicios formativos

| Proyecto | Área | Contenido |
|---|---|---|
| [`audit-shopcloud-cloud-assessment`](./audit-shopcloud-cloud-assessment) | Vulnerability Assessment | Escaneo y priorización de vulnerabilidades (WPScan) sobre un entorno WordPress de laboratorio; análisis CVE con criterios CVSS/PR/privilegios. |
| [`audit-fortune-bank-compliance`](./audit-fortune-bank-compliance) | Risk Assessment (MAGERIT v3) | Propagación de impacto entre activos dependientes y cálculo de riesgo residual tras aplicar salvaguardas. |
| [`sec-hardening-network-labs`](./sec-hardening-network-labs) | Risk Assessment (MAGERIT v3 / ENS) | Valoración de activos y cálculo de impacto repercutido sobre un escenario de administración pública. |
| [`sec-vulnerability-management-assessment`](./sec-vulnerability-management-assessment) | Vulnerability Management | Priorización y mitigación de hallazgos reales contra NIST NVD. |
| [`sec-infrastructure-evaluation`](./sec-infrastructure-evaluation) | Seguridad lógica | Evaluación de control de accesos y seguridad lógica sobre una infraestructura corporativa simulada. |
| [`sec-applied-defensive-operations`](./sec-applied-defensive-operations) | Defensive Operations | Evaluación de riesgos aplicada sobre infraestructura de red y seguridad lógica. |
| [`sec-advanced-threat-mitigation`](./sec-advanced-threat-mitigation) | Threat Mitigation | Auditoría de seguridad sobre una plataforma web corporativa. |
| [`sec-threat-hunting-operations`](./sec-threat-hunting-operations) | Threat Hunting | Valoración de activos y caza de amenazas aplicando MITRE ATT&CK. |
| [`secops-monitoring-soc-labs`](./secops-monitoring-soc-labs) | SOC / Monitorización | Investigación de un contenedor Docker no autorizado en un servidor de producción — triage, contención y análisis. |
| [`secops-incident-forensics-ir`](./secops-incident-forensics-ir) | Forense / IR | Desglose de un incidente complejo: cadena de ataque, evidencia y lecciones aprendidas. |
| [`sec-gamified-defense-drills`](./sec-gamified-defense-drills) | Blue Team (gamificado) | Ejercicios defensivos interactivos en Python. |
| [`secops-cli-automation`](./secops-cli-automation) · [`automation-bash-scripting`](./automation-bash-scripting) | Automatización | Scripts Bash de administración, permisos y automatización de tareas SecOps. |
| [`core-cybersecurity-fundamentals`](./core-cybersecurity-fundamentals) · [`core-infosec-governance`](./core-infosec-governance) | Fundamentos / Gobierno | Fundamentos de ciberseguridad y gobierno de la seguridad de la información. |
| [`knowledge-base-engineering`](./knowledge-base-engineering) | Base de conocimiento | Apuntes técnicos de referencia (incl. stack Microsoft/Azure). |
| [`profile-career-roadmap`](./profile-career-roadmap) | — | CV y plan de carrera. |

---

## 🛠️ Stack técnico

**Seguridad ofensiva / recon:** Nmap · Burp Suite · OWASP ZAP · Metasploit · OpenVAS · WPScan · Kali Linux
**SOC / Monitorización:** Splunk · Elastic Stack · Kibana · Microsoft Sentinel · Sysmon · Datadog · Grafana
**Metodologías:** MAGERIT v3 · ENS (RD 311/2022) · ISO/IEC 27001:2022 · NIST SP 800-115 · MITRE ATT&CK · CIS Controls v8 · PTES · OWASP WSTG
**Normativa:** RGPD/LOPDGDD · LSSI-CE · NIS2
**Plataformas / lenguajes:** Linux · Windows · Python · Bash · SQL · REST APIs · HTTP/S · DNS · TCP/IP · Git

## 📫 Contacto

[LinkedIn](https://www.linkedin.com/in/xaviermargaleftech/) · [margalef.xr@gmail.com](mailto:margalef.xr@gmail.com) · Barcelona, España
