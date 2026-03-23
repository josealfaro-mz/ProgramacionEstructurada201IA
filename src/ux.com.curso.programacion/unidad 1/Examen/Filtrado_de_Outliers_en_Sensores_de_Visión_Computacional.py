# Un sistema de percepción robótica toma 10 lecturas de confianza de un sensor de profundidad.
# Diseñar un algoritmo que calcule el promedio de las lecturas que se 
# encuentren dentro del "Rango de Inferencia Válido" (entre 65% y 85% de precisión, ambos inclusive). 
# Las lecturas fuera de este rango deben ser consideradas como
# ruido u outliers y deben ser ignoradas para el cálculo del promedio final.

def lectura():
    suma = 0
    contador = 0
    
    for i in range(10):
        valor = float(input("Ingresa la lectura en %: "))
        if lectura_es_valida(valor):
            suma += valor
            contador += 1
        elif lectura_es_outlier(valor):
            print(f"Lectura fuera de rango: {valor}%")
    
    return suma, contador

def lectura_es_valida(lectura):
    return lectura >= 65 and lectura <= 85

def lectura_es_outlier(lectura):
    return lectura < 65 or lectura > 85

def analizar_lecturas(suma, contador):
    if contador > 0:
        promedio = suma / contador
        return promedio
    else:
        return None

def promedio_final():
    suma, contador = lectura()
    promedio = analizar_lecturas(suma, contador)
    
    if promedio is not None:
        print("Promedio de lecturas válidas:", promedio)
    else:
        print("No hubo lecturas válidas")

if __name__ == "__main__":
    promedio_final()