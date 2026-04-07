"""
    Algoritmo para el calculo del fondo de ahorro
"""

def fondos():
    saldo = 0
    meta = 1000
    while saldo < meta:
        deposito = int(input("Ingrese el deposito actual: "))
        saldo += deposito
        return saldo
    
def main():
    resultado = fondos()
    print("Meta superada $", resultado)

if __name__ == "__main__":
    main()