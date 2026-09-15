import sys

# Para algunos del bonus he utilizado IA para acabar

"""
El módulo sys en Python proporciona acceso a varios parámetros 
y funciones del sistema, especialmente útiles para interactuar 
con el intérprete
 
https://docs.python.org/es/3.10/library/sys.html
"""
 
# help(sys)

def rectangle(x, y, tipo="A"):
    # Normas: Si x o y son menores que 1, no se imprime nada
    if x < 1 or y < 1:
        return
    
    # Bonus
    if tipo == "B":
        esquina = "B"
        horizontal = "/"
        vertical = "/"
        relleno = " "
    elif tipo == "C":
        esquina = "O"
        horizontal = "x"
        vertical = "x"
        relleno = "O"
    else: 
        esquina = "o"
        horizontal = "-"
        vertical = "|"
        relleno = " "
    
    if x == 1:
        linea_bordes = esquina
        linea_centro = vertical
    else:
        linea_bordes = esquina + horizontal * (x - 2) + esquina  
        linea_centro = vertical + relleno * (x - 2) + vertical

    if tipo == "C" and x >= 3:
        linea_bordes = "O" + "x" * ((x - 3) // 2) + "A" + "x" * ((x - 3) // 2) + "O"
        linea_centro = "x" + "O" * ((x - 3) // 2) + "B" + "O" * ((x - 3) // 2) + "x"

    # Prints
    if y == 1:
        print(linea_bordes)
    else:
        print(linea_bordes)
        for i in range(y - 2):
            print(linea_centro)
        print(linea_bordes)
        

def main():
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            
            if len(sys.argv) == 4:
                tipo = sys.argv[3]
            else:
                tipo = "A"
                
            rectangle(x, y, tipo)
        except ValueError:
            print("Los argumentos deben ser números enteros")
    else:
        print("Uso: python play_game.py <ancho> <alto> [tipo]")       

"""
Este bloque se asegura de que la función `main()` solo se ejecute 
cuando este archivo se ejecuta directamente desde la línea de comandos, 
y no cuando se importa como módulo en otro archivo
"""
 
if __name__ == "__main__":
    main()