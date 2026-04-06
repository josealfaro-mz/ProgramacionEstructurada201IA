'''
Objetivo: Implementar en Python el algoritmo de acumulación 
numérica siguiendo estrictamente la lógica de repetición definida en el diagrama de flujo proporcionado.
'''

suma = 0

def leer_numero():
    numero = int(input("Ingrese un número (0 para finalizar): "))
    return numero
while suma <= 500:
    numero = leer_numero()
    if numero == 0:
        break
    suma += numero
print("La suma acumulada es:", suma)

def main():
    pass    

if __name__ == "__main__":
    main()
