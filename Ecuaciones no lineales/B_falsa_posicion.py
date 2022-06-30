# Algoritmo Posicion Falsa

from math import *

def pol(x):
    '''
    Funcion de prueba
    '''
    return x ** 3 + 4 * x ** 2 - 10  # retorna pol(x) = x^3 + 4x^2 − 10


def trig(x):
    return x*cos(x-1) - sin(x)  # retorna trig(x) = xcos(x-1) - sin(x)


def pote(x):
    return pow(7, x) -13    # retorna pote(x) = 7^x - 13


def regula(f, p0, p1, tol, n):
    '''
    :param f:   funcion
    :param p0:  aproximacion inicial
    :param p1:  aproximacion final
    :param tol: tolerancia
    :param n:   iteraciones
    :return:    p aproximacion a 0 de f
    '''
    i = 0
    while i <= n:
        q0 = f(p0)
        q1 = f(p1)
        p = p1 - (q1*(p1-p0))/(q1 - q0)
        print("Iteracion => {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p-p1) < tol:
            return p
        i += 1
        q = f(p)
        if q*q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    print("Iteraciones agotadas....")
    return None


print("Falsa posicion: pol(x) = x^3 + 4x^2 − 10")
regula(pol, 1, 2, 1e-8, 100)

print("Falsa posicin: trig(x) =  xcos(x-1) - sin(x)")
regula(trig, 4, 6, 1e-8, 100)
# potencia
print("Falsa posicion: pote(x) = 7^x - 13")
regula(pote, 0, 2, 1e-8, 100)