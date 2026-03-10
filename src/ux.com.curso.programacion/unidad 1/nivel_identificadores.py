# Ejemplo para visualizar la identacion en Python

def explicar_indetificacion():
    # nivel 1
    mensaje ="Nivel 1 de indentificacion"
    print(mensaje)

    puntos =10

    if puntos >9:
        #nivel 2
        print("Entrar al flujo de if")

        if puntos ==10:
            # Nivel 3
            print("Puntos es igual a 10")

    #cierre nivel 1
def main():
    explicar_indetificacion()

    if __name__ == "__main__":
        main()