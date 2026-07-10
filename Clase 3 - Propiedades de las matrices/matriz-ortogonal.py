#Matrices ortogonales son aquellas que cumplen la propiedad de que su transpuesta es igual a su inversa, es decir,
# AA^T = A^-1. Esto implica que al multiplicar una matriz ortogonal por su transpuesta se obtiene la matriz identidad. 
# Las matrices ortogonales preservan longitudes y ángulos, lo que las hace útiles en diversas aplicaciones, 
# como en transformaciones lineales y análisis de datos.

import numpy as np
# Definir una matriz ortogonal A
A = np.array([[1, 0], [0, -1]])
# Calcular la transpuesta de A
A_T = np.transpose(A)
# Calcular la inversa de A
A_inv = np.linalg.inv(A)
# Verificar la propiedad de ortogonalidad
if np.array_equal(A_T, A_inv):
    print("La matriz A es ortogonal.")