# MATRIZ INVERSA

# Librerias
import string
import numpy as np
from scipy import linalg

# declarando matriz A (3x3)
A = np.array([[2, -1, 1],
              [3, 1, -2],
              [-1, 2, 5]])
# Calcular la inversa  B = A^(-1)
B = linalg.inv(A)

print("----------Matriz original----------")
print(A)
print()
print("----------Matriz inversa-----------")
print(B)
