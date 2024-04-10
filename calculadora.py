# sumar, restar, dividir, multiplicar, raiz cuadrada, y exponente
def sumar (x, y):
    res = x + y
    return x + y

# *args es una lista 
def sumador( *args):
    resultado= 0 
    for x in args:
        resultado += x


def restar (x, y): 
    return x - y 

def multiplicar (x, y):
    return x*y

def dividir(x, y):
    if (y != 0):
        return x/y 
    else: 
        print( " no se puede dividie entre cero")

print( sumar(5, 7))
print(restar(17, 6))
print(multiplicar(15, 3))
print(dividir(45, 5))
