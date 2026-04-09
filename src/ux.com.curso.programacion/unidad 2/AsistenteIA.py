# AsistenteIA.py
# Simulación de un asistente de voz basado en niveles de confianza (NLP)

# 1. Configuración del sistema
UMBRAL_ALTO = 80.0
UMBRAL_MINIMO = 40.0

# 2. Captura de datos del usuario
instruccion = input("Instrucción recibida: ")
confianza = float(input("Nivel de confianza calculado (%): "))

# 3. Lógica del asistente
if confianza >= UMBRAL_ALTO:
    print(f"Ejecutando la acción: {instruccion}... (Éxito)")
elif UMBRAL_MINIMO <= confianza < UMBRAL_ALTO:
    print(f"Confianza insuficiente. ¿Se refiere a: {instruccion}? Por favor confirme.")
else:  # confianza < UMBRAL_MINIMO
    print("Error 404: No pude entender la instrucción. Intente hablar más claro.")

# 4. Simulación de optimización (mensaje adicional)
if confianza > 95.0:
    print("Aviso: El modelo ha sido reforzado con éxito debido a la alta precisión.")

# 5. Cierre del proceso
print("Sesión de procesamiento finalizada.")