"""
monitor_ia.py
Monitor de Salud y Rendimiento para Clúster de Deep Learning
"""

def mostrar_estado_sistema(temperatura, memoria, enfriamiento):
    """
    Evalúa las condiciones del servidor y retorna el diagnóstico correspondiente.
    
    Parámetros:
        temperatura (float): Temperatura de la GPU en °C
        memoria (int): Porcentaje de uso de VRAM (0-100)
        enfriamiento (str): 'si' o 'no' indicando si el enfriamiento líquido está activo
    
    Retorna:
        str: Mensaje de diagnóstico
    """
    
    # Gestión de errores: Validar rango de memoria VRAM
    if memoria < 0 or memoria > 100:
        return "Error: Lectura de memoria fuera de rango (0-100%)."
    
    # CRÍTICO: Apagado inmediato
    if temperatura > 90 or memoria == 100:
        return "¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos."
    
    # PRECAUCIÓN: Temperatura elevada
    if 75 <= temperatura <= 90:
        if enfriamiento == "no":
            return "Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento."
        elif enfriamiento == "si":
            return "Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling)."
    
    # ESTADO ÓPTIMO
    if temperatura < 75 and memoria < 80:
        memoria_libre = 100 - memoria  # Reto adicional
        return f"Sistema Estable: Entrenamiento en curso a máxima capacidad.\nMemoria VRAM libre: {memoria_libre}% - Puedes cargar otro modelo si lo deseas."
    
    # Caso no contemplado explícitamente (por si hay combinaciones raras)
    return "Estado no clasificado. Revisa los parámetros manualmente."


def main():
    """
    Función principal que maneja la entrada del usuario y muestra el diagnóstico.
    """
    print("--- TELEMETRÍA DE CLUSTER IA ---\n")
    
    # Captura de datos con manejo básico de errores de tipo
    try:
        temperatura = float(input("Temperatura actual (°C): "))
        memoria = int(input("Uso de Memoria VRAM (%): "))
        enfriamiento = input("¿Enfriamiento activo? (si/no): ").strip().lower()
        
        # Validación de entrada para enfriamiento
        if enfriamiento not in ["si", "no"]:
            print("Error: Responde únicamente con 'si' o 'no'.")
            return
        
        # Obtener diagnóstico
        diagnostico = mostrar_estado_sistema(temperatura, memoria, enfriamiento)
        
        print("\n> Diagnóstico:", diagnostico)
        
    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos para temperatura y memoria.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()