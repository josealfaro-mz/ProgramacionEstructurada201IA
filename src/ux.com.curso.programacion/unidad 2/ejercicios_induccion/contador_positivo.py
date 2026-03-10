# Desarrollo de algoritmo Contador de Positivos

def contador_positivo():
    contador = 0
    while True:
        numero = int(input("Ingrese un numero (-1 para terminar): "))
        if numero <0:
            break
        contador += 1

    print("Cantidad de numeros positivos ingresados: ", contador)

# Definicion de la funcion main (Controla el flujo del programa)
def main():
    print("Bienvenido al contador de positivos")
    contador_positivo()

# Llamada la funcion main para iniciar el programa
if __name__ == "__main__":
    main()