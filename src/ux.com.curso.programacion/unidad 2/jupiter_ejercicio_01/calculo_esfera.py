#Calculo det radio de una esfera
import math

def define_esfera():
    radio = float(input("Ingrese el radio de la esfera en cm: "))
    volume = (4/3) * math.pi * (radio ** 3)
    print("El volumen de la esfera es:", volume, "cm cubicos")

def main():
    define_esfera()

if __name__ == "__main":
    main()