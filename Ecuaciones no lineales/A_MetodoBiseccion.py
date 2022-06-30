from math import *


def pol(x):
    '''Funcion de prueba'''
    return x**3 + 4*x**2 -10    # retorna polinomio de pol(x) = x^3 + 4x^2 -10

def trig(x):
    '''Funcion de prueba'''
    return x*cos(x-1) - sin(x)  # Retorna trig(x) = xcos(x-1) - sen(x)

def bisec(f, a, b, tol, n):
    '''
    Implementacion del metodo de biseccion
    Entradas:
        f   -- funcion
        a   -- inicio del intervalo
        b   -- fin del intervalo
        tol -- tolerancia
        n   -- numero maximo de iteraciones
    Salida:
        p aproximacion a cero de f
        None en caso de iteraciones agotadas
    '''
    i = 1
    while i <=n:
        p = a + (b-a) / 2
        print("i = {0:<2}, p = {1:.12f}".format(i,p))
        if abs(f(p)) <= 1e-15 or (b-a)/2 < tol:
            return p
        i += 1
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p
    print("Iteraciones agotadas: Error!")
    return None

# pol(x), a=1, b=2, Tol = 10^-8, N0 = 100
print("Biseccion Funcion pol(x) = x^3 + 4x^2 -10: ")
bisec(pol, 1, 2, 1e-8, 100)

# trig(x), a = 4, b = 6, Tol=10^-8, N0 = 100
print("Biseccino funcion trig(x) = xcos(x-1) - sen(x): ")
bisec(trig, 4, 6, 1e-8, 100)