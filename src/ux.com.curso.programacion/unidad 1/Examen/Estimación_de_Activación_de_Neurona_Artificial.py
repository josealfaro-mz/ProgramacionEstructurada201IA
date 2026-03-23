# Diseñar un algoritmo que calcule el valor de Activación (Z) de una neurona simple antes de pasar por su función no lineal. 
# El programa debe solicitar al usuario el valor del "Peso de entrada" (w) y el valor del "Dato de entrada" (x). 
# Aplica el modelo de regresión simple Z = w * x (asumiendo un sesgo/bias de cero).

# Activación de neurona artificial (modelo lineal)

w = float(input("Ingresa el peso (w): "))
x = float(input("Ingresa el dato de entrada (x): "))

Z = w * x

print("La activación de la neurona es:", Z)