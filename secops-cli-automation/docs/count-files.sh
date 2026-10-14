#!/bin/bash
# Cuenta las entradas (ficheros y directorios) del directorio actual, recursivamente.
find . | wc -l | tr -d ' '
