def normalizar_mensaje(texto):
    texto = texto.lower()
    texto = texto.strip()
    return texto

def detectar_intencion(mensaje):
    if "encender" in mensaje or "activar" in mensaje or "reproducir" in mensaje:
        return "COMANDO DE ACCION"
    elif "ayuda" in mensaje or "error" in mensaje or "fallo" in mensaje:
        return "REPORTE DE SOPORTE"
    else:
        return "CONSULTA GENERAL"

def main():
    print("ANALIZADOR DE INTENCIONES - ASISTENTE IA")
    mensaje = input("Ingrese comando de voz: ")
    
    mensaje_normalizado = normalizar_mensaje(mensaje)
    
    categoria = detectar_intencion(mensaje_normalizado)
    
    longitud = len(mensaje)
    
    print("\n--- PROCESANDO POR IA ---")
    print("Mensaje Normalizado:", mensaje_normalizado)
    print("Categoria de Intencion:", categoria)
    print("Longitud del mensaje:", longitud, "caracteres")
    print("--------------------------")

if __name__ == "__main__":
    main()


