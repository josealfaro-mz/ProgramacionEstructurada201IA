import math

# demostracion del uso de funciones de math

def mostrar_funciones_math(numero):
    #Crear una variable

    sen_x = math.sin(numero)
    conse_x = math.cos(numero)
    # Calcular la tangente usando la función tan de math
    tan_x = math.tan(numero)

    print("El seno de", numero, "es:", sen_x)
    print("El coseno de", numero, "es:", conse_x)
    # Imprimir la tangente calculada
    print("La tangente de", numero, "es:", tan_x)   

    resultado = sen_x + conse_x ** 2
    resultado_tan = sen_x + conse_x ** 2 + tan_x

    print("El resultado de sen^2 + cos^2 es:", resultado)
    print("El resultado de sen^2 + cos^2 + tan^2 es:", resultado_tan)

def main():
    numero = float(input("Ingrese un numero: "))
    mostrar_funciones_math(numero)

if __name__ == "__main__":
    main()