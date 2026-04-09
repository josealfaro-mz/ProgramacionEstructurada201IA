# Inicialización de variables
total_acumulado = 0
semanas = 0
meta = 2500

# Ciclo de control: mientras no se haya alcanzado o superado la meta
while total_acumulado < meta:
    # Lectura del salario semanal
    salario_semanal = float(input("Ingrese el salario de la semana: "))
    
    # Actualización del total acumulado
    total_acumulado = total_acumulado + salario_semanal
    
    # Incremento del contador de semanas
    semanas = semanas + 1

# Mostrar resultado final
print("Semanas trabajadas:", semanas)