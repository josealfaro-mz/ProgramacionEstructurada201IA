# Implementacion de Match en Python

def demostracion():
    print("-- Ejercicio de dias --")
    opcion = input("Ingrese un dia de la semana (1-7):")

    match opcion:
        case "1":
            print("Lunes")
            print(f"Hola!, hoy es lunes")
        case "2":
            print("Martes")
            print(f"Hola!, hoy es martes")
        case "3":
            print("Miercoles")
            print(f"Hola!, hoy es miercoles")
        case "4":
            print("Jueves")
            print(f"Hola!, hoy es jueves")
        case "5":
            print("Viernes")
            print(f"Hola!, hoy es viernes")
        case "6":
            print("Sabado")
            print(f"Hola!, hoy es sabado")
        case "7":
            print("Domingo")
            print(f"Hola!, hoy es domingo")
        case _:
            print("Dia no valido")

def main():
    demostracion()

if __name__ == "__main__":    
    main()