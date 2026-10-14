#!/bin/bash
# Lista el contenido del directorio actual ordenado por fecha (más reciente primero),
# marcando los directorios con "/", en una sola línea separada por espacios.
ls -ctp | tr '\n' ' '
