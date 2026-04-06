'''
Objetivo: Implementar en Python el algoritmo de suma condicional siguiendo
estrictamente la lógica de validación de entrada definida en el diagrama de flujo proporcionado.
'''

suma = 0

def leer_numero():
    return int(input("Ingrese un número: "))

while True:
    numero = leer_numero()
    
    if numero >= 10 and numero <= 50:
        suma += numero
    else:
        break

print("La suma acumulada es:", suma)

def main():
    pass

if __name__ == "__main__":
    main()