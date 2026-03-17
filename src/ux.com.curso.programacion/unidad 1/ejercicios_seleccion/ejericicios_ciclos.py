# Ejemplo de repeticion

def ejemplo_for():
    print("Estructura FOR")
    
    # For para iterar listas
    frutas = ["manzana", "banana", "naranja"]

    for fruta in frutas:
        print(fruta)

    #  For para iterar rangos
    for i in range(1, 5):
        print(i)

    # For para iterar rangos con pasos
    for i in range(0, 10, 2):
        print(i)

# Ejemplo de While
def ejemplo_while():
    print("Estructura WHILE")

    contador = 0
    
    while contador < 5:
        print(contador)
        contador += 1

# Simulacion de Do While
def ejemplo_do_while():
    print("Simulacion de Do While")
    
    secreto = "python12"
    intentos = 0

    while True:
        intentos_usuario = input("Ingresa la contraseña: ")  # Entrada real del usuario
        intentos += 1

        if intentos_usuario == secreto:
            print("¡Acceso concedido!")
            break  # Salir del bucle si la contraseña es correcta
        else:
            print("¡Acceso denegado! Intentalo de nuevo.")
    
    print(f"Número de intentos: {intentos}")

def main():
    ejemplo_for()
    print("\n")
    ejemplo_while()
    print("\n")
    ejemplo_do_while()

if __name__ == "__main__":
    main()