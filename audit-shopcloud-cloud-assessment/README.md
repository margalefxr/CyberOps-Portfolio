# ShopCloud · Vulnerability Assessment (WordPress / e-commerce)

**Metodología:** escaneo con WPScan, cruce de versiones contra NVD/Wordfence, priorización por CVSS + explotabilidad real.
**Qué se hizo:** identificación de componentes vulnerables en una tienda WordPress/WooCommerce (WP File Manager, Really Simple SSL, Jetpack) y selección razonada del CVE que cumple los criterios de impacto exigidos (privilegios altos, impacto contenido → CVE-2024-31229 sobre WP File Manager, no la RCE más vistosa).
**Resultado clave:** el riesgo más alto no es el plugin más famoso, sino el que combina versión desactualizada + vector de explotación realista para el contexto.

## Más allá del ejercicio: software supply chain y RGPD

Un e-commerce WordPress es, en la práctica, un ensamblaje de **software de terceros** (CMS, plugins, tema, pasarela de pago) que la tienda no desarrolla ni controla directamente — exactamente el tipo de superficie que hoy cubre el **Cyber Resilience Act (CRA)** de la UE para fabricantes de software y que las organizaciones gestionan con un **SBOM** (Software Bill of Materials) y una política de parcheo con SLA por criticidad, no con escaneos puntuales. Si la tienda procesa datos de clientes (nombre, dirección, historial de compra, pago), cualquier explotación de estos CVE deja de ser solo un problema técnico: activa las obligaciones de notificación del **RGPD Art. 33/34** (72h a la AEPD) y, si hay pago con tarjeta, **PCI-DSS**. La lección de mercado: gestión de vulnerabilidades y gestión de proveedores de software no son dos disciplinas separadas — son la misma superficie de riesgo vista desde dos ángulos (GRC y seguridad ofensiva).
