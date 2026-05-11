# Sistema de Reconocimiento de Patrones Biométricos

def main():
    print("--- ESCÁNER BIOMÉTRICO DE IA ---\n")
    
    # Configuración del Patrón Maestro (Base de Datos)
    patron_maestro = [1, 0, 1, 1, 0]
    
    # Captura de Datos del Sensor
    lectura_sensor = []
    
    print("Por favor, ingrese los 5 bits del escáner biométrico (0 o 1):")
    for i in range(5):
        while True:
            try:
                bit = int(input(f"Ingrese bit {i+1}: "))
                if bit in [0, 1]:
                    lectura_sensor.append(bit)
                    break
                else:
                    print("Error: Solo se permiten valores 0 o 1. Intente nuevamente.")
            except ValueError:
                print("Error: Ingrese un número entero (0 o 1).")
    
    print("\n> Comparando lectura con base de datos...")
    
    # Capa de Análisis (Procesamiento de IA)
    coincidencias = 0
    for i in range(5):
        if patron_maestro[i] == lectura_sensor[i]:
            coincidencias += 1
    
    porcentaje_similitud = (coincidencias / 5) * 100
    
    print(f"> Coincidencias encontradas: {coincidencias}")
    print(f"> Porcentaje de Similitud: {porcentaje_similitud}%")
    
    # Reto Adicional: Mostrar ambas listas
    print("\n--- COMPARACIÓN DETALLADA ---")
    print(f"Patrón Maestro: {patron_maestro}")
    print(f"Lectura Sensor:  {lectura_sensor}")
    
    # Mostrar dónde hubo errores
    print("Comparación posición por posición:")
    for i in range(5):
        if patron_maestro[i] == lectura_sensor[i]:
            print(f"Posición {i+1}: ✓ Coincide ({patron_maestro[i]} = {lectura_sensor[i]})")
        else:
            print(f"Posición {i+1}: ✗ DIFIERE (Maestro: {patron_maestro[i]}, Sensor: {lectura_sensor[i]})")
    
    # Toma de Decisiones (Salida)
    print("\n--- RESULTADO FINAL ---")
    if porcentaje_similitud == 100:
        print("ESTADO: ACCESO TOTAL: Identidad Verificada.")
    elif 60 <= porcentaje_similitud < 100:
        print("ESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")
    else:  # porcentaje_similitud < 60
        print("ESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")

if __name__ == "__main__":
    main()