"""
asistente_logico.py
Mi primer clasificador de intenciones para un asistente virtual
"""

# Importo el módulo datetime para poder trabajar con fechas y horas
# datetime es una herramienta que viene con Python
from datetime import datetime

# Le pongo un nombre a mi asistente
nombre_asistente = "IA-UX"

# Muestro un mensaje de bienvenida
print("Bienvenido al asistente " + nombre_asistente)
print("------------------------------------------")
print("Las funcuones unicas que tengo por ahora son: hola, clima y hora")

# Le pregunto al usuario qué necesita
frase = input("¿En qué puedo ayudarte hoy?: ")

# Convierto la frase a minúsculas para que sea más fácil comparar
# Esto hace que "HOLA" y "hola" sean lo mismo
frase = frase.lower()

# Aquí empiezo a revisar qué quiere el usuario

# Primero reviso si es un saludo
if "hola" in frase or "buenos dias" in frase:
    print("¡Hola! Soy tu asistente. Es un gusto saludarte.")

# Si no es saludo, reviso si pregunta por el clima
elif "clima" in frase or "temperatura" in frase:
    print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")

# Si no es clima, reviso si pregunta por la hora
elif "hora" in frase or "tiempo" in frase:
    # datetime.now() - Esto obtiene la fecha y hora actual de mi computadora
    # .strftime("%H:%M:%S") - Esto formatea la hora para que se vea bonito
    # %H es la hora (0-23), %M son los minutos, %S son los segundos
    hora_actual = datetime.now().strftime("%H:%M:%S")
    
    # Muestro la hora que obtuve del sistema
    print("La hora actual del sistema es: " + hora_actual)

# Si no es ninguna de las anteriores, no entiendo lo que dice
else:
    print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")

# Al final, siempre muestro este mensaje de despedida
print("")
print("Proceso finalizado. Gracias por usar " + nombre_asistente)