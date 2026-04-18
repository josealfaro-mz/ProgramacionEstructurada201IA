# ClasificadorObjetos.py
# Sistema de inspección de calidad para línea de producción

# Declaración de constantes
UMBRAL_PEQUENO = 5.0  # centímetros
UMBRAL_GRANDE = 20.0  # centímetros

def clasificar_objeto(dimension):
    """
    Función que clasifica el objeto según su dimensión
    
    Parámetros:
    dimension (float): Tamaño del objeto en centímetros
    
    Retorna:
    tuple: (clasificacion, volumen) donde volumen es None si no aplica
    """
    
    # Caso 1: Error de sensor
    if dimension <= 0.0:
        return "Error: Lectura inválida. Verifique el sensor.", None
    
    # Caso 2: Pequeño
    elif dimension > 0.0 and dimension <= UMBRAL_PEQUENO:
        return "Clasificación: Micro-componente (Grado A)", None
    
    # Caso 3: Mediano
    elif dimension > UMBRAL_PEQUENO and dimension <= UMBRAL_GRANDE:
        return "Clasificación: Componente Estándar (Grado B)", None
    
    # Caso 4: Grande
    elif dimension > UMBRAL_GRANDE:
        volumen = dimension ** 3  # dimensión al cubo
        return "Clasificación: Componente Industrial (Grado C)", volumen

def main():
    """
    Función principal del programa
    """
    # Entrada de datos
    dimension = float(input("Ingrese el tamaño del objeto detectado (cm): "))
    
    # Llamar a la función de clasificación
    mensaje, volumen = clasificar_objeto(dimension)
    
    # Imprimir resultado de clasificación
    print(mensaje)
    
    # Si hay volumen calculado (objeto industrial), mostrarlo
    if volumen is not None:
        print(f"Espacio requerido en contenedor: {volumen} cm3")
    
    # Salida Final
    print("Registro de inspección completado.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()