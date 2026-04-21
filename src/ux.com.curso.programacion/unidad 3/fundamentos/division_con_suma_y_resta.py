def division_entera(dividendo, divisor):
    if divisor == 0:
        return "Error: No se puede dividir entre cero"
    
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    
    resto = dividendo
    return cociente, resto

# Ejemplo de uso
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

resultado = division_entera(dividendo, divisor)
if type(resultado) == str:
    print(resultado)
else:
    cociente, resto = resultado
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")
