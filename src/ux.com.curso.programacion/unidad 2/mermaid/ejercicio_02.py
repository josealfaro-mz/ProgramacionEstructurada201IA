"""
Implementar en Python el algoritmo para calcular el Factorial de un número,
 siguiendo estrictamente la lógica definida en el Diagrama de Flujo proporcionado.
"""

def leer_n():
    n = int(input("Ingrese un número entero: "))
    return n

def factorial(n):
    factorial_n = 1
    i = 1
    while i <= n:
        factorial_n *= i
        i += 1
    return factorial_n
    while i >= n:
        print("El número debe ser mayor o igual a 0.")
        return None


def main():
    n = leer_n()
    resultado = factorial(n)
    if resultado is not None:
        print(f"El factorial de {n} es: {resultado}")

if __name__ == "__main__":
    main()
