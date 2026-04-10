# Calculo de Identidad Trigonometrica
import math

x= 42
numero_radianes= math.radians(x)
seno_x = math.sin(numero_radianes)**2
coseno_x = math.cos(numero_radianes)**2
identidad = seno_x + coseno_x

print(f"Para x = {x} grados: (Sin x)2 + (Cos x)2 = {identidad}")