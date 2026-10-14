# Fortune Bank · Risk Assessment (MAGERIT v3 — propagación de impacto)

**Metodología:** MAGERIT v3 / ENS — valor propio vs. valor acumulado, propagación de impacto entre activos dependientes, cálculo de impacto residual tras aplicar salvaguardas.
**Qué se hizo:** modelado de una cadena de dependencias (sistema core de transferencias → middleware → servidor físico) y cuantificación de cómo una degradación del 50% en el servidor de soporte se propaga hasta el servicio de negocio, con y sin salvaguardas al 50% de eficacia.
**Resultado clave:** el activo que hay que proteger primero no siempre es el que da la cara al cliente (el sistema core), sino el nodo de infraestructura del que depende todo lo demás — el clásico punto único de fallo (SPOF).

## Más allá del ejercicio: GRC en el sector financiero y riesgo de terceros

En banca, este ejercicio deja de ser un cálculo académico en el momento en que ese "servidor físico" es, en la mayoría de bancos reales, infraestructura **gestionada por un proveedor cloud o de datacenter externo**. Ahí entra en juego el **DORA** (Digital Operational Resilience Act, aplicable a entidades financieras de la UE desde 2025), que exige precisamente este tipo de análisis — mapeo de dependencias críticas, pruebas de resiliencia operativa y gestión del riesgo de proveedores TIC terceros — como obligación regulatoria, no como buena práctica opcional. La propagación de impacto que aquí se calcula a mano con MAGERIT es, en una auditoría DORA real, lo que un **registro de dependencias de terceros críticos** documenta de forma continua. Saber hacer este cálculo manualmente es lo que permite, después, entender (y auditar) si la herramienta de GRC de un banco lo está calculando bien.
