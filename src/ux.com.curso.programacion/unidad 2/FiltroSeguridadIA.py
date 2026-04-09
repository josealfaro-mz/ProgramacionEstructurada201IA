# FiltroSeguridadIA.py
# Simulación de filtrado y normalización de lecturas de un sensor térmico

# 1. Declaración de constantes
LIMITE_SUPERIOR = 100.0
LIMITE_INFERIOR = 0.0

def validar_lectura(lectura):
    """Verifica si la lectura está dentro del rango permitido"""
    return LIMITE_INFERIOR <= lectura <= LIMITE_SUPERIOR

def normalizar_dato(lectura):
    """Normaliza la lectura a un valor entre 0.0 y 1.0"""
    return lectura / LIMITE_SUPERIOR

def procesar_sensor():
    """Función principal que captura, valida y normaliza la lectura"""
    # 2. Entrada de datos
    lectura = float(input("Ingrese la lectura del sensor térmico: "))
    
    # 3. Validación y Procesamiento (Lógica de IA)
    if validar_lectura(lectura):
        # Datos válidos: normalización
        dato_normalizado = normalizar_dato(lectura)
        print(f"Señal aceptada. Valor normalizado para el modelo: {dato_normalizado}")
    else:
        # Datos no válidos
        print("Error: Lectura fuera de rango. La señal se considera ruido.")
    
    # 4. Salida Final
    print("Fin del proceso de filtrado de datos.")

# Punto de entrada del programa
if __name__ == "__main__":
    procesar_sensor()