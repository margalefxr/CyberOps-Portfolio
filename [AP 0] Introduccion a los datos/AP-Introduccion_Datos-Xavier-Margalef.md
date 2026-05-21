# Informe Técnico: AP Introducción a los Datos
**Analista:** Xavier Margalef  
**Fecha:** 2026-05-20  
**Clasificación:** Interna / Formación

## AP 1.1 | Estudio de Producción
### Análisis
¿Cuánto tiempo exacto tardará en completarse la descarga? De archivo de 500.235 KiB con descarga de 600 Mbps y sobrecarga overhead de 8%.

| Tamaño Original | 500.235 KiB |
| Calculo | 500.235 KiB x 1024 bytes = 512.240.640 bytes, 512.240.640 bytes/1.000.000 = 512,24 MB |
| Tamaño en MB | 512.24 MB  |
| Overhead (8%) | 600 Mbps x **0,08** = 48 Mbps, 600 - 48 = 552 Mbps, pasamos a MB para igualar al archivo 552 Mbps/8 = 69MB/s
| Aprendizaje clase | *Realmente no le podemos restar el 8% a la linea de 600 pq la linea tiene ese ancho de banda lo que hay que calcular es el 8% de mas al archivo original*
| **Tiempo de Transferencia** | **512,24MB/69 MB/s = 7,42 secs** |
| **Tiempo de Transferencia V2** | **512,24MB x 0,08 = 40,97 = 553,21989** luego 600mbps/8 = 75 MB/s luego** 553,21989/75 = 7,37 segundos** |

## AP 1.2 | Creador de contenido
### Análisis
Tiempo en segundos de subida de un archivo MP4 

| Tamaño Original | Video de 2,5 GB MP4 |
| Vel. subida | 50 Mbps |
| Calculo a MB | 2,5 GB x 1000 = 2.500 MB osea el video pesa **2.500 MB** |
| Calculo velocidad | 50 Mbps / 8 = **6,25 MB**, la velocidad de subida en MB |
| Calculo tiempo de subida real | 2.500 MB/6,25 MB/s = 400 secs, dividimos peso archivo por velocidad en MB/s |
| **Tiempo de Transferencia** + **Peso archivo** | **400 segundos** y **2.500 MB** |

## AP 1.3 | Descarga de pelicula
### Análisis
Tiempo en segundos de subida de un archivo MP4 

| Tamaño Original | Blue Ray de 15.8 GB |
| Vel. real bajada | 1 Gbps |
| Calculo a MB | Considerando megabyteMB$10^6 = 1.000.000$gigabyteGB$10^9 = 1.000.000.000$ **pues 15,8 GB x 1000 = 15.800 MB** |
| Calculo tiempo | como esta en bits pasamos a bytes con /8 entonces **1 Gbps / 8 = 0,125 Gigabytes x sec GB/s** |
| Igualar formatos | pasamos de Gigabyte a MB el tiempo osea 0,125 x 1000 = 125 MB/s |
| Calculo tiempo bajada | 15.800 / 125 MBs = 126,4 seegunos |
| **Tiempo de Transferencia** + **Blueray en MB** | **126,4 secs de tiempo descarga** y **15.800 MB pesa el archivo** |

## AP 1.4 | Backup de base de datos
### Análisis
Conversion archivo txt en MB a kB y GB y tiempo de descarga con 250 Mbps 


| Tamano archivo | txt de 10.485 MB |
| Velocidad bajada de red | 250 Mbps, atento al b que es bit no byte |
| Calculo de MB a kB | Considerando que **kiloByte esta una por debajo le damos 1000 asi que 10.485 MB x 1000 = 10.485.00 kB** |
| Calculo de MB a GB | Como esta **una por arriba le dividimos 1000 > 10.485 MB / 1.000 = 10,485 GB** |
| Tiempo descarga a MB  | Como esta en Mbps pasamos a MB, **250 Mbps/8 - 31,25 MBs** |
| Tiempo real descarga |10.485 MB / 31,25 MBs = 335,52 secs |
| **Resultados conversion y tiempo** | **10.485.000 kB** y **10,485 GB** y **335,52 segundos de descarga** |


## AP 1.5 | RAW
### Análisis
Conversion archivo RAW de MiB a Gibibytes y calculo transferencia por puerta velocidad


| Tamano archivo | RAW de 28.672 MiB |
| Velocidad transmision puerto | 5 Gbps |
| Calculo de MiB a Gibibytes | Considerando que **gibibyte esta una por encima q mebibyte hay que dividir 28.672 MiB / 1024 = 28 GiB** |
| Conversion de Gbps a GB | **Si son 5 Gbps tenemos q pasar a bytes asi que 5Gbps / 8 = 0,625 GBs, luego a MBs, 0,625 x 1000 = 625 MB/s** |
| Tiempo transferencia por puerto | 28.672 MiB / 625 MB/s = 45,8 segundos |
| **Resultados conversion y tiempo transferencia** | **28GiB** y **45,8 segundos transferencia**  |


## AP 1.6 | Auditoría de red
### Análisis
Encontramos sequencia binaria pura de 16 bits que es dirección MAC necesitamos convertirla a hexadecimal para analizarla en Wireshark.

| Tamano archivo| 1011011011110010 sequencia binaria pura de 16 bits  |
| Logica conversion a hexadecimal para Wireshark | Dividir 1011 | 0110 | 1111 | 0010 teniendo en cuenta pesos 8 4 2 1 convertimos |
| Calculo conversion a hexadecimal | 1011 es 1x8, 0x4, 1x2, 1x1 **queda 11 que en hexadecimal es B** pq numericamente va de 0 a 9> repetimos con los siguientes 3 bloques
| Explicacion clase | **Actua como array donde [4, 2, t, 9] la posicion 0 es la 1a, el 4, la posicion 1 es 2 pq al final es un indice diccionario y los sistemas como el hexadecimal siguen esa base**
| Conversion a hexadecimal | 11=B, 6=6, 15=F, 2=2 que da **B6F2** |
| **Resultados conversion** | **B6F2** |


## AP 1.7 | Analista SOC 
### Análisis
Analista SOC revisa script malicioso que ofusca la IPv4 para evadir cortafuegos y los EDR y AV, hay que convertirlo para anadir la IP real al firewall.

| Contexto buscado similitud realidad | Desofuscación de una dirección IP (Dotted Decimal a Hexadecimal/Binario). En operaciones, esto es crítico cuando
 analizas logs de firewall (iptables o nftables) o cabeceras de paquetes crudas donde la IP no aparece en formato legible, sino en formato Hexadecimal o Entero.
| IP sacada del script | 0127.0250.0100.0012, **el prefijo 0 indica que el numero esta en octal** |
| Logica para desofuscar | Dividir en bloques de 4  1011 | 0110 | 1111 | 0010 teniendo en cuenta pesos 8 4>
| Calculo conversion a hexadecimal | 1011 es 1x8, 0x4, 1x2, 1x1 **queda 11 que en hexadecimal es B** pq numericam>
| Explicacion clase | **Actua como array donde [4, 2, t, 9] la posicion 0 es la 1a, el 4, la posicion 1 es 2 pq a>
| Conversion a hexadecimal | 11=B, 6=6, 15=F, 2=2 que da **B6F2** |



## AP 1.8 | Investigador de ciberseguridad
### Análisis
Pishing contiene enlace sospechoso que para saltarse filtros seguridad usa ofuscacion de IP mixta.


| Contexto buscado similitud realidad | La diferencia fundamental entre el 1.7 y el 1.8 es la heterogeneidad.
 En el 1.7, todos los octetos estaban en la misma base (octal). En el 1.8, el atacante usa una "mezcla de sistemas" (hexadecimal y octal) para complicar la detección. |
| Enlace a analizar que contiene ofuscacion de IP | http://0xC6.063.100.0x1B/login.php, **aqui como mezcla varios sistemas hay que identificar cada seccion e identificar que sistema usa** |
| Identificar sistemas usados en ofuscacion de IP | Dividir en bloques y **ver el prefijo > 0xC6 como es 0+numero es hexadecimal, 063 como empieza 0 es octal y 100 es decimal**
| Tabla traduccion para descifrar | Si el bloque de 2 digitos es hexadecimal osea 0x (esto solo indica que es hexa no es valor numerico) el primer digito pesa 16 y el segundo pesa 1 |
si el bloque de dos digitos es ocal osea empieza por 0 solo, el siguiente digito pesa 8 y el segundo 1
| Aplicar logica traduccion a la IP | Bloque **0xC6 es hexa y la C es 12 y pesa 16 y el 6 es 6 y pesa 1** asi que 192
, luego el bloque **063 es octal y el 6 pesa 8 y el 3 1 asi que 51**, el **bloque 100 es decimal y se queda asi**,
y el bloque **0x1B es hexa y el 1 es 1 y pesa 16 y la B es 11 y pesa 1 asi que 27** |
| **Resultado final** | **192.51.100.27 IP real**

