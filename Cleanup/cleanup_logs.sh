#!/bin/bash
# Limpiar logs mayores a 7 días
echo "Iniciando limpieza de seguridad..."
find /var/log -name "*.log" -mtime +7 -exec rm {} \;
echo "Limpieza finalizada: $(date)" > log_report.txt
echo "Reporte generado."
