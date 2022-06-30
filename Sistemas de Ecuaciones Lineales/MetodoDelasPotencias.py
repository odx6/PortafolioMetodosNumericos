import numpy as np
from numpy import linalg

M = np.array([2., 1., 1. , 1.]).reshape(2, 2)
print(M)



v = np.array([1, 1.])

print(v)
print(np.dot(M, v))



M.shape

def metodo_de_potencias(M):
    
    L = M.shape[0]
    
    v = np.ones(L)
    v_vieja = np.array(np.zeros(L))
    
    eps = 1e-15
    
    while linalg.norm(v - v_vieja) > eps:
        v_vieja = v
        v = np.dot(M, v)
        v /= linalg.norm(v)
        
        #print v
        
    return v

print(metodo_de_potencias(M))

M = np.diag([1., 2, 3])

print(metodo_de_potencias(M))

from numpy import random

M = random.rand(100, 100)
M = M + M.T

v = metodo_de_potencias(M)

print(np.dot(M, v) / v)
