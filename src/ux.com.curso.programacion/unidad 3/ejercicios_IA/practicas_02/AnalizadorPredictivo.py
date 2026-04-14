# --- SISTEMA DE MONITOREO INDUSTRIAL ---
 
def limpiar_dato(lectura):
    """
    FUNCIÓN 1: Recibe un string del archivo, lo convierte a float.
    Si el dato es > 100 o < 0, devuelve None (Ruido detectado).
    """
    # IMPLEMENTAR AQUÍ
    try:
        valor = float(lectura)

        if valor < 0 or valor > 100:
            return None
        
        return valor
 
    except ValueError:
        return None
 
def calcular_alerta(valor_normalizado):
    """
    FUNCIÓN 2: Recibe el valor (0.0 a 1.0).
    Devuelve 'CRÍTICO' si es > 0.8, 'PRECAUCIÓN' si es > 0.5,
    y 'NORMAL' en cualquier otro caso.
    """
    # IMPLEMENTAR AQUÍ
    if valor_normalizado > 0.8:
        return 'CRÍTICO'
    elif valor_normalizado > 0.5:
        return 'PRECAUCIÓN'
    else:
        return 'NORMAL'
 
 
def obtener_estadisticas(lista_datos):
    """
    Universidad de Xalapa
    Implementación de un Pipeline de Procesamiento
    FUNCIÓN 3: Recibe la lista de datos válidos.
    Devuelve una TUPLA con: (Valor máximo, Valor mínimo, Promedio).
    """
    # IMPLEMENTAR AQUÍ
    if not lista_datos:
        return (0, 0, 0)
    
    maximo = max(lista_datos)
    minimo = min(lista_datos)
    promedio = sum(lista_datos) / len(lista_datos)

    return (maximo, minimo, promedio)
 
def generar_reporte(total_datos, validos, estadisticas):
    """
    FUNCIÓN 4: Imprime un resumen formateado de los resultados.
    """
    v_max, v_min, v_prom = estadisticas
    descartados = total_datos - validos
    # IMPLEMENTAR AQUÍ
    print("*" * 40)
    print("Reporte de analisis predictivo")
    print("*" * 30)
    print(f"Total de lecturas: {total_datos}")  #f en el print para formatear la salida
    print(f"Lecturas válidas: {validos}")
    print(f"Lecturas descartadas: {descartados}")
    print(f"Valor máximo: {v_max:.2f}")
    print(f"Valor mínimo: {v_min:.2f}") #2f es para mostrar solo 2 decimales
    print(f"Valor promedio: {v_prom:.2f}")
    print("*" * 30)

 
# --- LÓGICA PRINCIPAL (NO MODIFICAR ESTA PARTE) ---
def ejecutar_pipeline():
    datos_finales = []
    cuenta_total = 0
    with open("lecturas_sensores.txt", "r") as f:
        for linea in f:
            cuenta_total += 1
            valor = limpiar_dato(linea.strip())
            if valor is not None:
                # Normalizar para la IA (0-1)
                datos_finales.append(valor / 100)
    if datos_finales:
        stats = obtener_estadisticas(datos_finales)
        generar_reporte(cuenta_total, len(datos_finales), stats)
 
if __name__ == "__main__":
    ejecutar_pipeline()