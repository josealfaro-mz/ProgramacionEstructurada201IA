# acceso_biometrico.py

print("--- SISTEMA DE CONTROL BIOMÉTRICO ---")

# Solicitud de datos
nombre = input("Nombre del Ingeniero: ")
id_empleado = int(input("ID de Empleado: "))

iris = input("¿El escaneo de Iris coincide con la base de datos? (si/no): ").lower()
facial = input("¿El reconocimiento facial es mayor al 95%? (si/no): ").lower()

print("\n> Diagnóstico:")

# Validación de acceso
if id_empleado <= 0:
    print("¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía.")

elif iris == "si" and facial == "si":

    if id_empleado < 100:
        print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel SENIOR concedido a todas las áreas.")
    else:
        print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel JUNIOR concedido. Áreas de servidores restringidas.")

    # Reto adicional
    print(f"Generando log de entrada para el usuario: {id_empleado}...")

else:
    print("Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")