def declarar_estructuras():
    productos = ["Laptop", "Smartphone", "Tablet"]
    ventas = [[0] * 3 for _ in range(3)]
    return productos, ventas


def leer_datos(productos, ventas):
    for i in range(3):
        print(f"--- Registro para {productos[i]} ---")
        for j in range(3):
            ventas[i][j] = int(input(f"Ventas del día {j+1}: "))


def escribir_reporte(productos, ventas):
    print("\nRESUMEN DE VENTAS")
    total_general = 0

    for i in range(3):
        suma_producto = sum(ventas[i])
        total_general += suma_producto
        print(f"{productos[i]}: {ventas[i]} | Total: {suma_producto}")

    print(f"\nEl total de ventas de la semana es: {total_general}")
    print(f"El promedio de ventas es: {total_general / 9:.2f}")


def main():
    productos, ventas = declarar_estructuras()
    leer_datos(productos, ventas)
    escribir_reporte(productos, ventas)


if __name__ == "__main__":
    main()
