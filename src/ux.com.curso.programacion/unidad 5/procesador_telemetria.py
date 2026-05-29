# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================
import sys


# ==========================================
# FUNCIONES GENERADAS / ADAPTADAS CON IA
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Filtra una lista de lecturas de distancia del sensor LIDAR.

    Elimina los valores atípicos que se encuentran fuera del rango
    válido de 0.0 a 100.0, considerados errores de lectura del sensor.

    Parámetros:
        lista_datos (list): Lista de números flotantes con lecturas raw del LIDAR.

    Retorna:
        list: Nueva lista filtrada que contiene únicamente los valores válidos
              (0.0 <= valor <= 100.0).
    """
    lista_filtrada = []
    indice = 0
    while indice < len(lista_datos):
        valor = lista_datos[indice]
        if valor >= 0.0 and valor <= 100.0:
            lista_filtrada.append(valor)
        indice = indice + 1
    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta cuántas lecturas se encuentran por debajo del umbral crítico.

    Una lectura por debajo del umbral indica riesgo de colisión inmediata
    para el vehículo autónomo.

    Parámetros:
        lista_filtrada (list): Lista limpia de lecturas del LIDAR.
        umbral_critico (float): Distancia mínima segura en metros.

    Retorna:
        int: Número total de lecturas que representan riesgo de colisión.
    """
    total_alertas = 0
    indice = 0
    while indice < len(lista_filtrada):
        lectura = lista_filtrada[indice]
        if lectura < umbral_critico:
            total_alertas = total_alertas + 1
        indice = indice + 1
    return total_alertas


def generar_log_sistema(total_alertas):
    """
    Genera una cadena de texto con el reporte final del sistema de telemetría.

    Utiliza el módulo sys para detectar la plataforma del sistema operativo
    y determina si la operación del vehículo debe continuar o detenerse
    según el número de alertas críticas detectadas.

    Parámetros:
        total_alertas (int): Número de alertas críticas detectadas.

    Retorna:
        str: Cadena formateada con el log del sistema, indicando la plataforma,
             el total de alertas y la acción recomendada.
    """
    plataforma = sys.platform

    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    log = "[" + plataforma.upper() + "] Alertas críticas encontradas: " + str(total_alertas) + ". Acción: " + accion
    return log


# ==========================================
# PROGRAMA PRINCIPAL (Orquestación Manual)
# ==========================================
if __name__ == "__main__":
    # 1. Datos simulados de telemetría (con algunos errores de sensor)
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]
    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    # Paso 1: Limpiar lecturas inválidas
    lecturas_limpias = limpiar_lecturas(lecturas_raw)
    print("Lecturas raw:     ", lecturas_raw)
    print("Lecturas limpias: ", lecturas_limpias)

    # Paso 2: Calcular alertas usando las lecturas limpias
    num_alertas = calcular_alertas(lecturas_limpias, UMBRAL)
    print("Umbral crítico:   ", UMBRAL)
    print("Total de alertas: ", num_alertas)

    # Paso 3: Generar e imprimir el log del sistema
    log_final = generar_log_sistema(num_alertas)
    print("\n" + log_final)


"""
============================================================
EVIDENCIAS DE CONTROL DE CALIDAD
============================================================

--- 1. PROMPT UTILIZADO ---

Prompt para limpiar_lecturas:
"Actúa como un programador experto en Python Estructurado.
Escribe el código de una función llamada limpiar_lecturas.
Recibe como parámetro lista_datos (una lista de números flotantes
que representan lecturas del sensor LIDAR) y debe retornar una nueva
lista filtrada que contenga únicamente los valores en el rango 0.0 a 100.0.
Restricciones estrictas:
1. No utilices programación orientada a objetos (POO).
2. No utilices manejo de excepciones (nada de bloques try-except).
   Gestiona los datos usando condicionales if/else tradicionales.
3. No uses comprensión de listas (list comprehensions).
4. Usa un ciclo while con índice en lugar de for-in.
5. Incluye la documentación de la función mediante un Docstring descriptivo."

(El mismo formato se repitió para calcular_alertas y generar_log_sistema,
adaptando la descripción del parámetro y el retorno en cada caso.)


--- 2. TABLA DE PRUEBAS DE ESCRITORIO (TRACE TABLE) ---

Caso de prueba: TODAS las lecturas son erróneas o fuera de rango.
lista_datos = [-10.0, 150.0, -0.1, 200.5, -99.9]
UMBRAL = 5.0

PASO 1 — limpiar_lecturas([-10.0, 150.0, -0.1, 200.5, -99.9])

  indice=0  valor=-10.0   → -10.0 >= 0.0? NO  → no se agrega
  indice=1  valor=150.0   → 150.0 >= 0.0? SÍ, pero 150.0 <= 100.0? NO → no se agrega
  indice=2  valor=-0.1    → -0.1 >= 0.0? NO  → no se agrega
  indice=3  valor=200.5   → 200.5 >= 0.0? SÍ, pero 200.5 <= 100.0? NO → no se agrega
  indice=4  valor=-99.9   → -99.9 >= 0.0? NO  → no se agrega

  Retorna: []  ← lista vacía, todos eran errores de sensor

PASO 2 — calcular_alertas([], 5.0)

  La lista está vacía, el ciclo while no ejecuta ninguna iteración.
  total_alertas permanece en 0.

  Retorna: 0

PASO 3 — generar_log_sistema(0)

  plataforma = sys.platform  → ej. "WIN32" (depende del OS)
total_alertas = 0
0 > 3? NO → accion = "PERMITIDA"

  Retorna: "[WIN32] Alertas críticas encontradas: 0. Acción: PERMITIDA"

Conclusión: Con datos 100% inválidos el sistema los descarta todos,
no detecta alertas y permite la operación (correcto, no hay peligro real).


--- 3. AUDITORÍA DE CÓDIGO ---

Intento 1 — La IA generó las funciones usando comprensión de listas:
  lista_filtrada = [x for x in lista_datos if 0.0 <= x <= 100.0]

Corrección aplicada al prompt:
Se añadió la restricción explícita:
  "3. No uses comprensión de listas (list comprehensions).
   4. Usa un ciclo while con índice en lugar de for-in."

Con esas restricciones la IA produjo el ciclo while con índice que
aparece en el código final, el cual sí corresponde a la sintaxis
básica y estructurada vista en clase.

No se detectó uso de bibliotecas externas, try-except, ni POO.
La función generar_log_sistema sí utiliza sys (biblioteca estándar),
lo cual está explícitamente permitido por la práctica.
============================================================
"""
