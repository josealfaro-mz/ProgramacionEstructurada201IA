"""
Funcion que recibe un texto y decide que responder.
Implementa Programacacion Estrucutura pura.
"""

def procesar_pregunta(mensasje_usuario):
   #1.Normalizacion (Paso fundamental en IA)
   mensaje = mensaje_usuario.lower().strip()
   
   #2.Base de conocimiento (Diccionario)
    conocimiento = 
   {
      #Concepto de Estructura de Control
            "if": "La sentencia 'if' es una condicional. Pemite que el programa
        'tome decisiones basandose en una condicion booleana.", 

    #Tipos de Datos
        "int": "Reperesenta un numero entero (ej.5, -10, 0). No tienen parte decimal.",
    
    #Funciones y modularidad
        "def":"Es la palabra reservada para definir una funcion en python",
    
    #Operadores y Sintaxis
        "print":"Funcion que muestra informacion en la consola o salida"
        "estandar",
    
    #Conceptos de Programacion Estructurada
        "algoritmo":"Es una serie de pasos ordenados"
        "Y finitos para resolver un problema"
    }   
    
    #3.Logica de busqueda
    for clave in conocimiento:
        if clave in mensaje:
            return conocimiento[clave]

    return "Lo siento, aun no se que es eso. !Preguntame sobre variables, funciones o estructuras de control!"

def main():
   print("Hola! Soy tu asistente de programacion. Preguntame sobre variables, funciones o estructuras de control.")
   while true:
        user_input = input("Alumno -> ")
        if user_input.lower() == "salir": break

        respuesta = procesar_pregunta(user_input)
        print("Agente -> " {respuesta}")


# Prueba local (Offline)
if __name__ == "__main__":
    main()