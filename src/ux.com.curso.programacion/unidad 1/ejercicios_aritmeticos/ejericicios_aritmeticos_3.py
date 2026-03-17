import math

# demostracion del uso de funciones de math

def mostrar_funciones_math(numero):
    #Crear una variable

    sen_x = math.sin(numero)
    conse_x = math.cos(numero)

    print("El seno de", numero, "es:", sen_x)
    print("El coseno de", numero, "es:", conse_x) 

    resultado = sen_x + conse_x ** 2

    print("El resultado de sen^2 + cos^2 es:", resultado)

def tan_x(numero):
    tan_x = math.tan(numero)
    print("El tangente de", numero, "es:", tan_x)
    resultado = tan_x ** 2 + 1
    print("El resultado de tan^2 + 1 es:", resultado)

def main():
    numero = float(input("Ingrese un numero: "))
    mostrar_funciones_math(numero)
    tan_x(numero)

if __name__ == "__main__":
    main()