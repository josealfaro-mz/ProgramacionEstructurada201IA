"""
Imprimir una tabla de multiplicar
    1   2   3   4   ... 15
*** **  **  **  **  ... **
1*  1   2   3   4   ... 15
2*  2   4   6   8   ... 30
3*  3   6   9   12  ... 45
4*  4   8   12  16  ... 60
.
"""

def generar_tabla():
    # Tablas de multiplicar de forma vertical
    for i in range(1, 16):
        for j in range(1, 16):
            print(f"{i*j:4}", end="")
        print()  # Salto de línea después de cada fila

if __name__ == "__main__":
    generar_tabla()

