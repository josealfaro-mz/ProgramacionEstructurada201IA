class MonitorEntrenamiento:
    def __init__(self, umbral_convergencia=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral_convergencia

    def registrar_epoca(self, valor_error):
        # Validar número negativo
        if valor_error < 0:
            raise ValueError("El error no puede ser negativo.")

        # Agregar al historial
        self.historial_errores.append(valor_error)

        # Verificar convergencia
        if valor_error < self.umbral_convergencia:
            print("[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión.")
        else:
            print("> Registro exitoso.")

def main():
    print("--- Iniciando Monitor de Red Neuronal ---\n")
    
    monitor = MonitorEntrenamiento(umbral_convergencia=0.01)
    
    # Registrar 5 épocas
    for i in range(1, 6):
        while True:
            entrada = input(f"Ingrese el error de la Época {i}: ")
            try:
                valor = float(entrada)
                monitor.registrar_epoca(valor)
                break  # Sale del bucle si todo es válido
            except ValueError as e:
                # Captura tanto letras como negativos (gracias al raise en registrar_epoca)
                print(f"> [ERROR] Entrada inválida. {e}")
                print("> Intente nuevamente.\n")
    
    # Resumen final
    print("\n--- Resumen de Entrenamiento ---")
    print(f"Historial: {monitor.historial_errores}")
    
    if monitor.historial_errores:
        promedio = sum(monitor.historial_errores) / len(monitor.historial_errores)
        mejor_error = min(monitor.historial_errores)
        print(f"Promedio de Error: {promedio:.4f}")
        print(f"Mejor resultado obtenido: {mejor_error}")
    else:
        print("No se registraron errores válidos.")

if __name__ == "__main__":
    main()