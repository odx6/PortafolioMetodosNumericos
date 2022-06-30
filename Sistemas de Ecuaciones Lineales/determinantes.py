5# Determinante de una matriz
import numpy as np
import functools


def det(matriz):
    orden = len(matriz)
    posdet = 0
    for i in range(orden):
        posdet += functools.reduce((lambda x, y: x * y), [matriz[(i + j) % orden][j] for j in range(orden)])
    negdet = 0
    for i in range(orden):
        negdet += functools.reduce((lambda x, y: x*y), [matriz[(orden-i-j)% orden][j] for j in range(orden)])
    return posdet - negdet


A = np.array([[2, -1, 1],
              [3, 1, -2],
              [-1, 2, 5]])

print(det(A))
