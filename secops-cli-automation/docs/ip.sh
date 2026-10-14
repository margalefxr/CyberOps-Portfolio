#!/bin/bash
# Lista las direcciones MAC (link/ether) de las interfaces de red del sistema.
ip link | grep "link/ether"
