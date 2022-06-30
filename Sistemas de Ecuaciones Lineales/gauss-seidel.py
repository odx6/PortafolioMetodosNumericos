# Metodo de gauss-Seidel


import numpy as np

# Entrada

A = np.array([[3., -0.1, -0.2],
              [0.1, 7, -0.3],
              [0.3, -0.2, 10]])

B = np.array([7.85, -19.3, 71.4])

x0 = np.array([0., 0., 0.])

tol = 0.00001  # tolerancia
i_max = 100  # iteraciones maximas

tam = np.shape(A)
n = tam[0]
m = tam[1]
# Valores iniciales
X = np.copy(x0)
diferencia = np.ones(n, dtype=float)
errado = 2 * tol

it = 0  # iteracion comienza en 0
while not (errado <= tol or it > i_max):
    # por fila
    for i in range(0, n, 1):
        # por columna
        suma = 0
        for j in range(0, m, 1):
            # excepto diagonal de A
            if (i != j):
                suma = suma - A[i, j] * X[j]

        nuevo = (B[i] + suma) / A[i, i]
        diferencia[i] = np.abs(nuevo - X[i])
        X[i] = nuevo
    errado = np.max(diferencia)
    it = it + 1

# Respuesta X en columna
X = np.transpose([X])

# Revisar si no converge
if it > i_max:
    X = 0
# Revisar respuesta
verifica = np.dot(A, X)

print('respuesta X: ')
print(X)
print('verificar A.X=B: ')
print(verifica)
