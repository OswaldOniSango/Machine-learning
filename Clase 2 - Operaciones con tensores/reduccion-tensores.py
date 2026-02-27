import numpy as np
import torch as torch
import tensorflow as tf
#La reduccion de un tensor es sumar todos los elementos de un tensor
#en un vector seria la sumatoria de x[i]
#en caso de una matriz seria la sumatorio de x[i][j]
#Reduccion por suma aparece mucho en el aprendizaje automatico, tambien se puede hacer
#maximo
#minimo
#media
#producto

array_np = np.array([[25,2],[5,26],[3,7]])
print("----------------Actual array------------------------------")
print(array_np)
print("----------------NUMPY reduccion------------------------------")
print("reduccion: ", array_np.sum())
print("reduccion sobre todas las filas se hace axis = 0: ", array_np.sum(axis=0))
print("reduccion sobre todas las columnas se hace axis = 1: ", array_np.sum(axis=1))
print("reduccion max: ", array_np.max())
print("reduccion min: ", array_np.min())
print("reduccion mean: ", array_np.mean())
print("reduccion prod: ", array_np.prod())


print("----------------PYTORCH reduccion------------------------------")
array_pt = torch.tensor([[25,2],[5,26],[3,7]])
print("reduccion: ", torch.sum(array_pt))
print("educcion sobre todas las filas se hace axis = 0: ", torch.sum(array_pt, 0))
print("reduccion sobre todas las columnas se hace axis = 1 :", torch.sum(array_pt, 1))
print("reduccion max: ", torch.max(array_pt))
print("reduccion min: ", torch.min(array_pt))
#mientras estudiaba me encontre con un error, e investigando me di cuenta
#que mi programa intentaba hacer una media y al obtener float rompia, ya que
#cuando lo cree arriba no habia especificado array_pt = torch.tensor([[25,2],[5,26],[3,7]])
#asi que para imprimir le especifico el tipo de dato en el metodo torch.mean(array_pt.float())
print("reduccion mean: ", torch.mean(array_pt.float()))
print("reduccion prod: ", torch.prod(array_pt))

print("----------------TENSORFLOW reduccion------------------------------")
array_tf = tf.Variable([[25,2],[5,26],[3,7]])
print("reduccion", tf.reduce_sum(array_pt))
print("reduccion sobre todas las filas se hace axis = 0: ", tf.reduce_sum(array_pt, 0))
print("reduccion sobre todas las columnas se hace axis = 1: ",tf.reduce_sum(array_pt, 1))
print("reduccion max: ", tf.reduce_max(array_tf))
print("reduccion min: ", tf.reduce_min(array_tf))
print("reduccion mean: ", tf.reduce_mean(array_tf))
print("reduccion prod: ", tf.reduce_prod(array_tf))


