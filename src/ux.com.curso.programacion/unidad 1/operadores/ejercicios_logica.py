# Ejercicio de operadores lógicos
from ast import main


def opereradores():
    a = True
    b = False

    print("a and b:", a and b)
    print("a or b:", a or b)
    print("not a:", not a)
    print("not b:", not b)

    numero_1 = 10
    numero_2 = 20

    if numero_1 > numero_2:
        print("numero_1 es mayor que numero_2")
    else:
        print("numero_1 es menor que numero_2")

def main():
    opereradores()

if __name__ == "__main__":
    main()