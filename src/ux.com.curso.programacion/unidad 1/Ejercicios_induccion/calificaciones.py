def leer_calificaciones():
    calificaciones = []
    for i in range(5):
        calificacion = float(input(f"Ingrese la calificación del estudiante {i + 1}: "))
        calificaciones.append(calificacion)
    return calificaciones

def calificacion(calif):
    if calif >= 90:
        print("A")
    elif calif >= 80:
        print("B")
    elif calif >= 70:
        print("C")
    elif calif >= 69:
        print("D")   
    else:
        print("F")

def main():
    print("La calificación de los estudiantes es:")
    calificaciones = leer_calificaciones()
    for i, calif in enumerate(calificaciones):
        print(f"Estudiante {i + 1}: {calif}")
        calificacion(calif)

        