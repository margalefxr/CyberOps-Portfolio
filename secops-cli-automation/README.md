# SecOps CLI Automation · Fundamentos de Linux

Ejercicios de administración básica en Linux: permisos de fichero (`chmod`), scripts simples en Bash (listado, conteo, info de red) y manejo del sistema de ficheros. Práctica de base, no automatización de seguridad en producción.

## Contenido

| Ruta | Qué demuestra |
|---|---|
| [`docs/linux.sh`](./docs/linux.sh) · [`count-files.sh`](./docs/count-files.sh) · [`ip.sh`](./docs/ip.sh) · [`play-ls.sh`](./docs/play-ls.sh) | Scripts Bash mínimos: info de sistema, conteo de ficheros, interfaces de red, listado ordenado por fecha |
| [`permissions-demo/docs/`](./permissions-demo/docs/) | Permisos reales aplicados: `editable.txt` (644), `solo-lectura.txt` (444, solo lectura), `script.sh` (755, ejecutable), `enlace` (symlink a `file1`) |

## Por qué sigue aquí

El control de permisos a nivel de fichero es, en miniatura, el mismo principio que el *least privilege* (PoLP) que se aplica después a gran escala en IAM/RBAC (ver `profile-career-roadmap` y la experiencia en Seccion9/Glovo) — y los scripts de aquí son la base de los que luego se usan para hardening post-auditoría.
