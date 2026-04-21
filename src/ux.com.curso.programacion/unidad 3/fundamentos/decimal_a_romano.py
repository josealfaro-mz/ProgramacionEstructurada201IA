def decimal_a_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letras = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    resultado = ""
    
    i = 0
    while i < len(valores):
        while numero >= valores[i]:
            resultado = resultado + letras[i]
            numero = numero - valores[i]
        i = i + 1
    
    return resultado

def main():
    print("CONVERSION DE DECIMAL A ROMANO")
    print("Rango permitido: 1 a 3000")
    
    numero = int(input("Ingrese un numero: "))
    
    if numero < 1 or numero > 3000:
        print("Error: El numero esta fuera del rango permitido")
    else:
        romano = decimal_a_romano(numero)
        print("El numero", numero, "en romano es:", romano)

if __name__ == "__main__":
    main()