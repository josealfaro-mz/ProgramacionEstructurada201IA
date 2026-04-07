
"""
Ejercicio: Acumulación Genérica
"""

def acumulacion():
    suma = 0
    while suma < 500:
        numero = int(input("Ingrese un número: "))
        suma += numero
    return suma

def main():
    resultado = acumulacion()
    print("La suma acumulada es:", resultado)

if __name__ == "__main__":
    main()