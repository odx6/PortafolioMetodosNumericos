import numpy as np
from lu import *
A =np.array([[1.0,2.0,-1.0],[2.0,1.0,-2.0],[-3.0,1.0,1.0]])
B = [1.0,-2.0,3.0]
L, U = lu_fac(A)

# sustitucion hacia adelante
size = A.shape[1]
X = np.zeros(size)
Y = np.zeros(size)
Y[0] = B[0]/L[0,0]
for i in range(1,size):
    sum = 0
    for j in range(i):
        sum += L[i,j]*Y[j]
    Y[i] = (B[i]-sum) / L[i,i]


# sustitucion hacia atras
X[size-1] = Y[size-1]/U[size-1,size-1]
for i in range(size-1,0,-1):
    sum = 0
    for j in range(size-1,i,-1):
        sum += U[i,j]*X[j]
    X[i] = (Y[i] - sum) / U[i,i]
print('la solucion del sistema es: ')    
print(X)

# verificamos que la solucion funciona: AX = B
print(np.matmul(A,X))

# empaquetamos ahora todo dentro de una funcion que efectue todo el proceso:
from lu import *
def lu_sol(A,B):
    L, U = lu_fac(A)
    size = A.shape[1]
    X = np.zeros(size)
    Y = np.zeros(size)
    Y[0] = B[0]/L[0,0]
    # sustitucion hacia adelante
    for i in range(1,size):
        sum = 0
        for j in range(i):
            sum += L[i,j]*Y[j]
        Y[i] = (B[i]-sum) / L[i,i]
    X[size-1] = Y[size-1]/U[size-1,size-1]
    # sustitucion hacia atras
    for i in range(size-1,0,-1):
        sum = 0
        for j in range(size-1,i,-1):
            sum += U[i,j]*X[j]
        X[i] = (Y[i] - sum) / U[i,i]
    return X
X = lu_sol(A,B)
print(X)
