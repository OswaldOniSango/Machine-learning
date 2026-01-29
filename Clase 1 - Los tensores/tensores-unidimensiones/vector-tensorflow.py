#Vectores
#Matrices unidimensionales de numero
#Representan un punto en el espacio
#Vector de longitud 2 que representan la ubicacion en la matriz 2D
#Longitud de 3 representa la ubicacion en el cubo 3D
#Longitud de n representan n dimensiones

#Transposicion
#transforma un vector de fila a columna, su notacion es [1,5]t

#Vectores (Tensor de rango 1)
import tensorflow as tf

array = tf.Variable([25, 2,5])
print(array)

#forma de ese arry
print(array.shape)

#tipo de arry
print(type(array))

#imprime el indice 0
print(array[0])

#tipo de dato del indice 1
print(type(array[0]))

#transponer
#array_t = array.T
#print(array_t)

#No transpone porque una matriz unidimensional
#el cual fue declarado con un corchete no tiene
#una segunda dimension para transponerla
#intentemos crear uno con dos corchetes (2da dimension)
array_d = tf.Variable([[25,4,6]])
array_d_t = tf.transpose(array_d) 
print(array_d)
print(array_d_t)
print(array_d.shape)
print(array_d_t.shape)

