print("--- SISTEMA DE FILTRADO DE DATOS (SENSOR GPU) ---\n")

# Declarar arreglo para 8 lecturas
temperaturas = []

# Ciclo para solicitar las 8 temperaturas
for i in range(8):
    lectura = float(input(f"Lectura {i+1}: "))
    temperaturas.append(lectura)

# Inicializar contador de errores
contador_errores = 0

# Detección y corrección de valores atípicos
for i in range(len(temperaturas)):
    if temperaturas[i] < 0 or temperaturas[i] > 100:
        temperaturas[i] = 35.0
        contador_errores += 1

# Mostrar cuántas correcciones se realizaron
print(f"\nSe detectaron {contador_errores} lecturas erróneas y fueron corregidas a 35.0.")

# Calcular promedio sin usar sum() ni len()
suma = 0
for temp in temperaturas:
    suma += temp

promedio = suma / 8

# Mostrar arreglo final
print(f"Datos limpios: {temperaturas}")
print(f"Promedio de operación: {promedio:.2f}°C")

# Regla de IA
if promedio > 75:
    print("ALERTA: Activando sistema de enfriamiento líquido")
else:
    print("Estado: Operación normal")