"""
Gamified Defense Drills - Ejercicio de fundamentos de Python

Dibuja un rectángulo en la terminal a partir de un ancho, un alto y un
tipo de borde opcional. Ejercicio introductorio de lógica de programa y
estructuras de control (no un ejercicio de seguridad ofensiva/defensiva
en sí mismo, pese al nombre del reto).

Uso: python play-game.py <ancho> <alto> [tipo]
  tipo: A (por defecto, bordes simples) · B (estilo alternativo) · C (bonus)
"""

import sys


def rectangle(x: int, y: int, tipo: str = "A") -> None:
    """Imprime un rectángulo de x columnas por y filas. No imprime nada si x o y < 1."""
    if x < 1 or y < 1:
        return

    if tipo == "B":
        esquina, horizontal, vertical, relleno = "B", "/", "/", " "
    elif tipo == "C":
        esquina, horizontal, vertical, relleno = "O", "x", "x", "O"
    else:
        esquina, horizontal, vertical, relleno = "o", "-", "|", " "

    if x == 1:
        linea_bordes = esquina
        linea_centro = vertical
    else:
        linea_bordes = esquina + horizontal * (x - 2) + esquina
        linea_centro = vertical + relleno * (x - 2) + vertical

    # Variante bonus del tipo C: marca el centro de cada línea con A/B
    if tipo == "C" and x >= 3:
        linea_bordes = "O" + "x" * ((x - 3) // 2) + "A" + "x" * ((x - 3) // 2) + "O"
        linea_centro = "x" + "O" * ((x - 3) // 2) + "B" + "O" * ((x - 3) // 2) + "x"

    if y == 1:
        print(linea_bordes)
    else:
        print(linea_bordes)
        for _ in range(y - 2):
            print(linea_centro)
        print(linea_bordes)


def main() -> None:
    if len(sys.argv) not in (3, 4):
        print("Uso: python play-game.py <ancho> <alto> [tipo]")
        return

    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    except ValueError:
        print("Los argumentos ancho y alto deben ser números enteros")
        return

    tipo = sys.argv[3] if len(sys.argv) == 4 else "A"
    rectangle(x, y, tipo)


if __name__ == "__main__":
    main()
