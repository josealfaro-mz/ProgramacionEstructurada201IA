""" Funcion que recibe un texto y decide que responder. Implementa Programacacion Estrucutura pura. """

def procesar_pregunta(mensasje_usuario):
    #1.Normalizacion (Paso fundamental en IA)
    mensaje = mensasje_usuario.lower().strip()

    #2.Base de conocimiento (Diccionario)
    conocimiento = {
        #Concepto de Estructura de Control
        "if": "La sentencia 'if' es una condicional. Permite que el programa tome decisiones basandose en una condicion booleana.",
        "while": "Es un ciclo que se repite mientras una condicion sea verdadera.",
        "for": "Es un ciclo que permite iterar sobre una secuencia (como listas o rangos).",
        "else": "Se ejecuta cuando la condicion del 'if' no se cumple.",

        #Tipos de Datos
        "int": "Representa un numero entero (ej.5, -10, 0). No tienen parte decimal.",
        "float": "Representa un numero con parte decimal (ej. 3.14, -0.001).",
        "str": "Representa una cadena de texto (ej. 'Hola', '123')",
        "bool": "Representa valores logicos: verdadero (True) o falso (False).",

        #Funciones y modularidad
        "def": "Es la palabra reservada para definir una funcion en python",
        "return": "Permite devolver un valor desde una funcion.",
        "parametros": "Son los valores que una funcion recibe para trabajar.",
        "argumentos": "Son los valores que se pasan a una funcion al momento de llamarla.",

        #Operadores y Sintaxis
        "print": "Funcion que muestra informacion en la consola o salida estandar",
        "input": "Permite al usuario ingresar datos desde el teclado.",
        "==": "Operador de comparacion que verifica si dos valores son iguales.",
        "+": "Operador que se utiliza para sumar valores.",

        #Conceptos de Programacion Estructurada
        "algoritmo": "Es una serie de pasos ordenados y finitos para resolver un problema",
        "variable": "Es un espacio en memoria donde se almacena un valor.",
        "condicion": "Es una expresion que puede ser verdadera o falsa.",
        "ciclo": "Es una estructura que permite repetir un bloque de codigo varias veces.",
    }

    #3.Logica de busqueda
    for clave in conocimiento:
        if clave in mensaje:
            return conocimiento[clave]

    return "Lo siento, aun no se que es eso. !Preguntame sobre variables, funciones o estructuras de control!"


def main():
    print("Hola! Soy tu asistente de programacion. Preguntame sobre variables, funciones o estructuras de control.")
    
    while True:
        user_input = input("Alumno -> ")
        if user_input.lower() == "salir":
            break

        respuesta = procesar_pregunta(user_input)
        print(f"Bot -> {respuesta}")


# Prueba local (Offline)
if __name__ == "__main__":
    main()