'''
Objetivo: Implementar en Python el algoritmo para generar una serie de números impares 
siguiendo estrictamente la lógica definida en el diagrama de flujo proporcionado.
'''

def leer_n():
    contador = 0
    numero = 1
    n = int(input("Ingrese un número entero positivo: "))
    while contador < n:
        print(numero)
        numero += 2
        contador += 1

def main():
    leer_n()
    
if __name__ == "__main__":    
    main()