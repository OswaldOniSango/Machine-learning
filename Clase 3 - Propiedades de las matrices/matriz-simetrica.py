import numpy as np
#Matriz simetrica
# Definir una matriz simetrica
A = np.array([[0, 1, 2],[1, 7, 8], [2, 8, 9]])
print("La matriz A es:\n", A)

# Verificar si la matriz es simetrica
if np.allclose(A, A.T):
    print("La matriz A es simetrica")
    print(A==A.T)
else:
    print("La matriz A no es simetrica")


##Matriz Identidad
# Definir una matriz identidad
# La matriz identidad es una matriz cuadrada en la que todos los elementos de la diagonal principal son iguales a 1 y todos los demás elementos son iguales a 0. La matriz identidad se denota comúnmente como I y tiene la propiedad de que cualquier matriz multiplicada por la matriz identidad permanece sin cambios.
I = np.eye(2)
print("La matriz identidad I es:\n", I)  

#Una matriz Identidad si la multiplicamos por otra matriz, el resultado es la misma matriz. Por ejemplo, si multiplicamos la matriz A por la matriz identidad I, obtenemos la misma matriz A:
A = np.array([[1, 2], [3, 4]])
C = np.dot(A, I)
print("El producto de la matriz A y la matriz identidad I es:\n", C)    

