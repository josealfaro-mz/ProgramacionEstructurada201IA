# simulador_acceso.py

def iniciar_sesion():
    intentos = 0
    clave_correcta = "1234"
    
    while intentos < 3:
        contrasena = input("Ingrese su contraseña: ")
        
        if contrasena == clave_correcta:
            print("Acceso Concedido")
            return True  # Éxito, salimos de la función
        else:
            intentos += 1
            print("Contraseña incorrecta")
    
    print("Cuenta bloqueada")
    return False  # Fallo por agotamiento de intentos

# Ejecutar el simulador
if __name__ == "__main__":
    iniciar_sesion()