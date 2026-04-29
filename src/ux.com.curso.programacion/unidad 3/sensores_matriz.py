print("--- MÓDULO DE SENSORES ---")
sensores = []
for i in range(5):
    sensores.append(float(input(f"Sensor {i+1}: ")))
promedio = sum(sensores)/5
print(f"Promedio: {promedio:.1f}m")
if promedio < 2:
    print("Aviso: Reduciendo velocidad")

print("\n--- MÓDULO DE VISIÓN ---")
matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Fila {i}, Col {j}: "))
        if valor > 255:
            valor = 255
        fila.append(valor)
    matriz.append(fila)

print("Matriz capturada:")
for fila in matriz:
    print(fila)

contador = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] > 200:
            contador += 1
print(f"Píxeles brillantes: {contador}")