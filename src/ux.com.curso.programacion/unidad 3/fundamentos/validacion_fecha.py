def es_bisiesto(año):
    """Determina si un año es bisiesto"""
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def fecha_valida(dia, mes, año):
    """Verifica si una fecha es válida"""
    # Validar año
    if año < 1:
        return False
    
    # Validar mes
    if mes < 1 or mes > 12:
        return False
    
    # Determinar días del mes
    if mes == 2:  # Febrero
        if es_bisiesto(año):
            dias_max = 29
        else:
            dias_max = 28
    elif mes in [4, 6, 9, 11]:  # Abril, junio, septiembre, noviembre
        dias_max = 30
    else:  # Enero, marzo, mayo, julio, agosto, octubre, diciembre
        dias_max = 31
    
    # Validar día
    if dia < 1 or dia > dias_max:
        return False
    
    return True

def main():
    """Función principal"""
    print("Validación de Fecha\n")
    
    # Leer datos del teclado
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    
    # Validar fecha
    if fecha_valida(dia, mes, año):
        print(f"\n La fecha {dia}/{mes}/{año} es VÁLIDA")
    else:
        print(f"\n La fecha {dia}/{mes}/{año} es INVÁLIDA")

if __name__ == "__main__":
    main()