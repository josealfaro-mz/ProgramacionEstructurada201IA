# --- ANALIZADOR DE SENTIMIENTOS IA ---
print("--- ANALIZADOR DE SENTIMIENTOS IA ---\n")

# Declaración del Vector de Características (inicializado con ceros)
puntajes_sentimiento = [0, 0, 0]

# Lectura y Escritura (Entrada de Datos) - procesar 5 palabras
for i in range(5):
    while True:
        try:
            clasificacion = int(input(f"Palabra {i+1} - Clasificación (0: Positivo, 1: Neutral, 2: Negativo): "))
            if clasificacion in [0, 1, 2]:
                break
            else:
                print("Error: Ingresa solo 0, 1 o 2")
        except ValueError:
            print("Error: Ingresa un número válido (0, 1 o 2)")
    
    # Incrementar el valor en la posición correspondiente
    puntajes_sentimiento[clasificacion] += 1

# Mostrar estado final del vector
print(f"\nEstado final del vector de características: {puntajes_sentimiento}")

# Operaciones sobre Arreglos (Análisis) - encontrar el índice con mayor valor
indice_mayor = 0
mayor_valor = puntajes_sentimiento[0]

for i in range(1, len(puntajes_sentimiento)):
    if puntajes_sentimiento[i] > mayor_valor:
        mayor_valor = puntajes_sentimiento[i]
        indice_mayor = i

# Toma de Decisión
print("\nResultado de IA:", end=" ")
if indice_mayor == 0:
    print("La frase es Positiva (Predominancia en índice 0)")
elif indice_mayor == 1:
    print("La frase es Neutral (Predominancia en índice 1)")
else:
    print("La frase es Negativa (Predominancia en índice 2)")