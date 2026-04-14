# piloto_automatico.py
# Simulación de un piloto automático para vehículo autónomo

# Configuración de Variables (Simulación de Sensores)
distancia = float(input("¿A qué distancia está el objeto más cercano (en metros)?: "))
color_semaforo = input("¿De qué color está el semáforo? (verde/amarillo/rojo): ").lower()
peaton = input("¿Hay un peatón cruzando? (si/no): ").lower()

# Lógica de Navegación (Estructuras Condicionales)

# Prioridad Máxima (Frenado de Emergencia)
if distancia < 5 or peaton == "si":
    print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")
# Regla del Semáforo
elif color_semaforo == "rojo":
    print("Estado: Detenido. Esperando luz verde.")
elif color_semaforo == "amarillo":
    print("Estado: Precaución. Reduciendo velocidad para detenerse.")
elif color_semaforo == "verde" and distancia >= 5:
    print("Estado: En movimiento. Todo despejado para avanzar.")
# Caso de Error en Sensores
elif color_semaforo not in ["verde", "amarillo", "rojo"]:
    print("Error de lectura en sensores: Color de semáforo no reconocido.")

# Resumen de Seguridad
print("Monitoreo de sensores constante... Sistema activo.")