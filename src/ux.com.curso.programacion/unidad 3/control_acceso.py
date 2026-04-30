class ControlAcceso:
    def __init__(self):
        # Diccionario con usuarios iniciales
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"[ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")

            # Extra: si es administrador puede agregar usuarios
            if rol == "Administrador":
                opcion = input("¿Desea agregar un nuevo usuario? (s/n): ")
                if opcion.lower() == "s":
                    nueva_matricula = input("Ingrese nueva matrícula: ")
                    nuevo_rol = input("Ingrese rol: ")
                    self.usuarios_autorizados[nueva_matricula] = nuevo_rol
                    print("Usuario agregado correctamente.")
        else:
            print("[ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")


# Programa principal
sistema = ControlAcceso()

print("--- Sistema de Seguridad Laboratorio IA - UX ---")

while True:
    try:
        matricula = input("\nIngrese su matrícula: ")

        if matricula == "":
            raise ValueError("Entrada vacía")

        sistema.verificar_permisos(matricula)

    except ValueError:
        print("Error: Debe ingresar una matrícula válida.")

    finally:
        print("--- Intento de acceso registrado en el log del servidor ---")