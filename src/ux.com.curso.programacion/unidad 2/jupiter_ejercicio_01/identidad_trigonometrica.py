# Calculo de Identidad Trigonometrica
import math

def calculo_identidad(x):
    numero_radianes= math.radians(x)
    seno_x = math.pow(math.sin(numero_radianes), 2)
    coseno_x = math.pow(math.cos(numero_radianes), 2)
    identidad = seno_x + coseno_x

    print(f"Para x = {x} grados: (Sin x)2 + (Cos x)2 = {identidad}")

def calculo_identidad_2(x):
    numero_radianes= math.radians(x)
    seno_x = math.pow(math.sin(numero_radianes), 2)
    coseno_x = math.pow(math.cos(numero_radianes), 2)
    identidad = seno_x + coseno_x

    print(f"Para x = {x} grados: (Sin x)2 + (Cos x)2 = {identidad}")

def main():
    x = int(input("Ingrese el valor de x en grados: "))
    calculo_identidad(x)
    calculo_identidad_2(x)

if __name__ == "__main__":
    main()