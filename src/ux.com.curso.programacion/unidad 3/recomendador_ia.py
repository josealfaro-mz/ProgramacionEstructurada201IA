# Listas de películas
peliculas_accion = ["Mad Max", "John Wick", "Inception"]
peliculas_comedia = ["Toy Story", "Minions", "Free Guy"]
peliculas_terror = ["It", "The Conjuring", "Saw"]

# Función de recomendación
def obtener_recomendacion(genero_elegido, edad_usuario):
    if edad_usuario < 13:
        return peliculas_comedia[0]
    
    if genero_elegido == "accion":
        return peliculas_accion[0]
    elif genero_elegido == "comedia":
        return peliculas_comedia[0]
    elif genero_elegido == "terror":
        return peliculas_terror[0]
    else:
        return "Género no válido"

# Función principal
def main():
    print("SISTEMA DE RECOMENDACIÓN IA v1.0")
    print("--------------------------------")

    edad = int(input("Ingrese su edad: "))
    genero = input("¿Qué género prefiere (accion/comedia/terror)?: ").lower()

    if edad < 13 and genero == "terror":
        print("\nNota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público.\n")

    recomendacion = obtener_recomendacion(genero, edad)

    print("Recomendación de la IA:", recomendacion)

# Punto de entrada del programa
if __name__ == "__main__":
    main()