#Matriz inversa 
# La matriz inversa de una matriz cuadrada A es otra matriz, denotada como A^(-1), 
# que cumple la propiedad de que cuando se multiplica por A, el resultado es la matriz identidad. 
# En otras palabras, si A es una matriz cuadrada y A^(-1) es su inversa, entonces:
# A * A^(-1) = A^(-1) * A = I
# La matriz inversa solo existe para matrices cuadradas que son no singulares, es decir , 
# matrices que tienen un determinante distinto de cero. Si una matriz no tiene inversa, se dice que es singular.
# La matriz inversa es el equivalente matricial al inverso de un numero.
# 5 * 5^(-1) = 1
# A * A^(-1) = I
# A^(-1) = 1 / determinante(A) * adjunta(A)
# adjunta(A) = transpuesta(cofactores(A))
import numpy as np
# Definir una matriz A
A = np.array([[4, 2], [-5, -3]])
# Calcular la matriz inversa de A
A_inv = np.linalg.inv(A)
print("La matriz inversa de A es:\n", A_inv)

#Si multiplicamos A por su inversa, obtenemos la matriz identidad
I = np.dot(A, A_inv)
print("El producto de A y su inversa es la matriz identidad:\n", np.round(I))
