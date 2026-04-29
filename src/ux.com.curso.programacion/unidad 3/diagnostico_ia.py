import math
from datetime import datetime

# Módulo de Visualización (Procedimiento - no devuelve nada)
def imprimir_encabezado():
    """Imprime el encabezdo del sistema (procedimiento sin retorno)"""
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    print("=" * 36)
    print("    SISTEMA DE SALUD INTELIGENTE")
    print("=" * 36)
    print(f"    Fecha: {fecha_actual}")
    print()

# Módulo de Cálculo de IMC (Función con retorno)
def calcular_imc(peso, estatura):
    """
    Calcula el Índice de Masa Corporal
    
    Args:
        peso (float): Peso en kilogramos
        estatura (float): Estatura en metros
    
    Returns:
        float: Valor del IMC
    """
    return peso / (estatura ** 2)

# Módulo de Análisis de Presión (Función con retorno)
def evaluar_presion(presion_sistolica):
    """
    Evalúa la presión sistólica del paciente
    
    Args:
        presion_sistolica (float): Valor de presión sistólica
    
    Returns:
        str: "Alta" si es > 140, "Normal" en caso contrario
    """
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"

# Módulo de entrada de datos (Función con retorno)
def obtener_datos_paciente():
    """
    Solicita los datos del paciente al usuario
    
    Returns:
        tuple: (nombre, peso, estatura, presion_sistolica)
    """
    nombre = input("Nombre del Paciente: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))
    presion_sistolica = float(input("Presión Sistólica: "))
    print()
    return nombre, peso, estatura, presion_sistolica

# Módulo de visualización de resultados (Procedimiento)
def mostrar_resultados(nombre, imc, estado_presion):
    """
    Muestra los resultados del análisis (procedimiento sin retorno)
    
    Args:
        nombre (str): Nombre del paciente
        imc (float): Valor del IMC
        estado_presion (str): Estado de presión ("Alta" o "Normal")
    """
    print("--- RESULTADOS DEL ANÁLISIS ---")
    print(f"Paciente: {nombre}")
    print(f"IMC Calculado: {math.ceil(imc)}")  # Redondeo hacia arriba con math.ceil
    print(f"Estado de Presión: {estado_presion}")
    print("-" * 31)

# Lógica Principal del Programa
def main():
    # Invocar encabezado
    imprimir_encabezado()
    
    # Obtener datos del paciente
    nombre, peso, estatura, presion_sistolica = obtener_datos_paciente()
    
    # Calcular IMC (llamada a función con retorno)
    imc = calcular_imc(peso, estatura)
    
    # Evaluar presión (llamada a función con retorno)
    estado_presion = evaluar_presion(presion_sistolica)
    
    # Mostrar resultados (procedimiento)
    mostrar_resultados(nombre, imc, estado_presion)

# Punto de entrada del programa
if __name__ == "__main__":
    main()