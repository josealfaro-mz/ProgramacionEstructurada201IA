"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte III)
Alumno: José Alberto Manzanilla Alfaro
"""
import math  # se agrego math para usar fabs y no calcular el absoluto a mano

# =====================================================================
# RETO 1: Inicializador de Tablero de Juego (Matrices)
# Sentido: Crear una cuadrícula vacía de 4x4 (como el juego 2048 o un tablero)
#          inicializada con ceros antes de colocar las piezas de la IA.
# Problema: Uso erróneo y peligroso de multiplicación de referencias,
#           o bucles anidados manuales sumamente redundantes.
# =====================================================================
def inicializar_tablero_vacio():
    # El novato descubrió que puede "multiplicar" listas, pero no sabe
    # el peligro de que todas las filas apunten a la misma dirección de memoria.
    fila_base = [0, 0, 0, 0]
    tablero = [fila_base, fila_base, fila_base, fila_base]
    
    # El novato intenta asegurarse de que funcione usando un ciclo manual 
    # para "limpiar" cada celda por si acaso, lo cual es redundante
    for i in range(4):
        for j in range(4):
            tablero[i][j] = 0
            
    return tablero

# se crea cada fila por separado para que no compartan la misma memoria
# asi si cambias una celda no afecta a todas las demas filas
def inicializar_tablero_vacio_refactorizado():
    fila1 = [0, 0, 0, 0]
    fila2 = [0, 0, 0, 0]
    fila3 = [0, 0, 0, 0]
    fila4 = [0, 0, 0, 0]
    tablero = [fila1, fila2, fila3, fila4]
    return tablero


# =====================================================================
# RETO 2: Recortador de Valores Atípicos (Clamping de Datos)
# Sentido: Limitar las señales de los sensores del robot a un rango seguro.
#          Si la señal baja de un mínimo o pasa de un máximo, se "recorta".
# Problema: Lógica condicional repetitiva y tosca que ignora funciones nativas.
# =====================================================================
def limitar_senal_sensor(valor_lectura, minimo, maximo):
    # Árbol de decisiones manual y enredado para simular un tope
    if valor_lectura < minimo:
        resultado = minimo
    else:
        if valor_lectura > maximo:
            resultado = maximo
        else:
            resultado = valor_lectura
            
    return resultado

# se quito el if-else anidado y se puso todo en un solo nivel
# primero se verifica si esta fuera de rango y se regresa directo
def limitar_senal_sensor_refactorizado(valor_lectura, minimo, maximo):
    if valor_lectura < minimo:
        return minimo
    if valor_lectura > maximo:
        return maximo
    return valor_lectura


# =====================================================================
# RETO 3: Buscador del Valor Más Cercano a Cero (Error Mínimo)
# Sentido: Encontrar el menor error absoluto (loss) en una lista de pruebas.
# Problema: Inicialización incorrecta o manual de infinitos y cálculo 
#           tosco del valor absoluto usando multiplicaciones por -1.
# =====================================================================
def buscar_error_minimo(lista_errores):
    # El novato inicializa el menor error con un número "grande" inventado
    menor_error = 999999.99 
    
    for i in range(len(lista_errores)):
        valor_actual = lista_errores[i]
        
        # Intento manual de obtener el valor absoluto (fabs)
        if valor_actual < 0:
            absoluto = valor_actual * -1
        else:
            absoluto = valor_actual
            
        if absoluto < menor_error:
            menor_error = absoluto
            
    return menor_error

# se cambio el 999999.99 por float('inf') que es el infinito de python
# asi no hay riesgo de que algun error sea mas grande que ese numero inventado
# tambien se uso math.fabs() en lugar del if para calcular el valor absoluto
def buscar_error_minimo_refactorizado(lista_errores):
    menor_error = float('inf')  # infinito real, no un numero inventado
    
    for valor_actual in lista_errores:
        absoluto = math.fabs(valor_actual)  # math.fabs hace lo mismo que el if de arriba
        if absoluto < menor_error:
            menor_error = absoluto
            
    return menor_error


# =====================================================================
# RETO 4: Filtro de Valores Únicos (Eliminador de Duplicados)
# Sentido: Limpiar las IDs de los usuarios del servidor de Discord para
#          que no se procesen comandos repetidos en el mismo ciclo.
# Problema: Algoritmo de búsqueda lineal doblemente anidado sumamente lento.
# =====================================================================
def depurar_usuarios_repetidos(lista_ids):
    lista_limpia = []
    
    # Recorrido manual buscando si el elemento ya existe antes de agregarlo
    for i in range(len(lista_ids)):
        id_actual = lista_ids[i]
        ya_existe = False
        
        for j in range(len(lista_limpia)):
            if lista_limpia[j] == id_actual:
                ya_existe = True
                break
                
        if not ya_existe:
            lista_limpia.append(id_actual)
            
    return lista_limpia

# se quito el doble for anidado, ahora solo se usa "in" para verificar
# si el id ya esta en la lista antes de agregarlo, es mas corto y legible
def depurar_usuarios_repetidos_refactorizado(lista_ids):
    lista_limpia = []
    
    for id_actual in lista_ids:
        if id_actual not in lista_limpia:  # "not in" reemplaza el segundo for
            lista_limpia.append(id_actual)
            
    return lista_limpia


# === PROGRAMA PRINCIPAL (Punto de entrada para probar) ===
if __name__ == "__main__":
    print("--- Probando Código Inicial (Parte III) ---")
    
    tablero_ia = inicializar_tablero_vacio()
    print("Tablero inicializado de 4x4:")
    for fila in tablero_ia:
        print(fila)
        
    print("Lectura recortada (125.4 en rango 0-100):", limitar_senal_sensor(125.4, 0.0, 100.0))
    
    errores_entrenamiento = [0.45, -0.12, 0.89, -0.03, 0.22]
    print("El error más cercano a cero es:", buscar_error_minimo(errores_entrenamiento))
    
    ids_discord = [4521, 8892, 4521, 1022, 8892, 9931]
    print("Lista de IDs únicas filtradas:", depurar_usuarios_repetidos(ids_discord))

    print("\n--- Probando Código Refactorizado (Parte III) ---")

    tablero_ref = inicializar_tablero_vacio_refactorizado()
    print("Tablero refactorizado de 4x4:")
    for fila in tablero_ref:
        print(fila)

    print("Lectura recortada refactorizada:", limitar_senal_sensor_refactorizado(125.4, 0.0, 100.0))
    print("Error mínimo refactorizado:", buscar_error_minimo_refactorizado(errores_entrenamiento))
    print("IDs únicas refactorizadas:", depurar_usuarios_repetidos_refactorizado(ids_discord))