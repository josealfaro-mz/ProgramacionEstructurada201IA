def pregunta_1():
    print(2**3**2)

def pregunta_2():
    x =10/2
    print(type(x))
"""
    x=1 x =1 x==x print(x==x) True
"""
def pregunta_3():
    x = 1 
    x=x 
    print(x==x)

def pregunta_4():
    print(1 // 2 * 3)

def pregunta_5():
    y = 2+3 * 5
    print(y)
"""
Concatenacion de cadenas entonces '1' + '2' es '12'
"""
def pregunta_6():
    a ='1'
    b = '2'
    print(a + b)
"""
Operador % devuelve el residuo de la division
entonces 11 dividido entre 3 es 3
con un residuo de 2 por lo tanto el resultado es 2
"""
def pregunta_7():
    z = 11 % 3
    print(z)
"""
El operador // devuelve el cociente de la division
entera
"""
def pregunta_8():
    x =5
    y =2
    print(x//y)

def pregunta_9():
    val = 10
    val +=5*2
    print(val)
"""
bool("") es  False porque una cadena vacia
se considera como False, mientras que bool(" ") es True porque una cadena con un espacio no esta vacia.
"""
def pregunta_10():
    print(bool(""),bool(" "),bool(0),bool(0.00))

def main():
    pregunta_1()
    pregunta_2()
    pregunta_3()
    pregunta_4()
    pregunta_5()
    pregunta_6()
    pregunta_7()
    pregunta_8()
    pregunta_9()
    pregunta_10()

if __name__ == "__main__":
    main() 