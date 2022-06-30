from math import *


def test1(t, y):
    '''Funcion de prueba'''
    # 10*sin(PI-t) -5y
    return y - t**2 + 1     # y' = y-t^2 +1


def test2(t, y):
    return 2 - exp(-4*t) - 2*y  # y' = 2 - e^-4t - 2y


def Euler(a, b, y0, f, N):
    '''
    :param a:   inicio
    :param b:   fin
    :param y0:  aproximacion inicial
    :param f:   funcion
    :param N:   pasos
    :return:    w  aproximacion final
    '''
    h = (b-a)/N
    t = a
    w = y0
    print("t0 = {0:.2f}, w0 = {1:.12f}".format(t,w))
    for i in range(1, N+1):
        w = w + h*f(t,w)
        t = a + i*h
        print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.12f}".format(i, t,  w))
    return w


# dy/dt = y - t^2 + 1, a=0, b=2, y0=0.5, N = 10
print("Metodo de Euler: y' = y-t^2 +1")
Euler(0,2,0.5, test1, 10)

# a = 0, b = 1, y0 = 1, N = 20
print("Metodo de Euler: y' = 2 - e^-4t - 2y")
Euler(0,1,1,test2, 20)