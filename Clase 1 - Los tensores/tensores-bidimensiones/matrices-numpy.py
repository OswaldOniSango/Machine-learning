import numpy as np

array = np.array([[25,2],[5,26],[3,7]])
print("La matriz es")
print(array)

print("La forma de la matriz: " )
print(array.shape)

print("La cantidad de elementos en la matriz:")
print(array.size)

#imprimimos toda la columna en el indice 1
print(array[:,1])
#imprimimos toda la fila en el indice 2
print(array[2,:])

#slicing by index:

print(array[0:2,0:2])
