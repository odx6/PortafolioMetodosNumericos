# INTERPOLACION

# Metodo de Newton - Diferencias divididas de newton

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Ingreso de datos
xi = np.array([3.2, 3.8, 4.2, 4.5])
fi = np.array([5.12, 6.42, 7.25, 6.85])

# Diferencias divididas avanzadas
titulo = ['i    ', 'xi    ', 'fi    ']
n = len(xi)
ki = np.arange(0,n,1)
tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
tabla = np.transpose(tabla)

# diferencias divididas vacias
dfinita = np.zeros(shape=(n,n), dtype=float)
tabla = np.concatenate((tabla,dfinita), axis=1)

# calcular tabla inicia en columna 3
[n,m] = np.shape(tabla)
diagonal = n-1
j = 3
while j<m:
    titulo.append('F['+str(j-2) + ']')
    i = 0
    paso = j-2 # inicia en 1
    while i < diagonal:
        denominador = (xi[i + paso] - xi[i])
        numerador = tabla[i + 1, j - 1] - tabla[i, j - 1]
        tabla[i, j] = numerador / denominador
        i = i + 1
    diagonal -= 1
    j += 1

# Polinomio de diferencias divididas
# caso: puntos equidistantes en eje x
dDividida = tabla[0,3:]
n = len(dfinita)


# expresion del polinomio con sympy
x = sym.Symbol('x')
polinomio = fi[0]
for j in range(1,n,1):
    factor = dDividida[j-1]
    termino = 1
    for k in range(0,j,1):
        termino = termino*(x-xi[k])
    polinomio = polinomio + termino*factor

# Simplifica multiplicando entre (x-xi)
polisimple = polinomio.expand()

# polinomio para evaluacion numerica
px = sym.lambdify(x, polisimple)

# Puntos para la grafica

muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a, b, muestras)
pfi = px(pxi)

# Salida
np.set_printoptions(precision = 4)
print('Tabla Diferencia Dividida')
print([titulo])
print(tabla)
print('dDividida: ')
print(dDividida)
print('polinomio: ')
print(polinomio)
print('polinomio simplificado: ' )
print(polisimple)

# Grafica
plt.plot(xi,fi, 'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Diferencias Divididas - Metodo de Newton')
plt.show()