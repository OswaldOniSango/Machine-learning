import numpy as np
import torch as torch
import tensorflow as tf

print("----------------NUMPY------------------------------")

array_np = np.array([[25,2],[5,26],[3,7]])
print("----------------Actual array------------------------------")
print(array_np)

array_p = array_np * 2
array_s = array_np + 2
array_r = array_np - 2
array_d = array_np / 2

print("----------------Multiplica por 2------------------------------")
print(array_p)
print("----------------Suma 2------------------------------")
print(array_s)
print("----------------resta 2------------------------------")
print(array_r)
print("----------------divide por 2------------------------------")
print(array_d)



print("----------------PYTORCH------------------------------")

array_pt = torch.tensor([[25,2],[5,26],[3,7]])

#de esta manera los operadores de python estan sobrecargados asi que usamos
array_p = array_pt * 2
array_s = array_pt + 2
array_r = array_pt - 2
array_d = array_pt / 2

print("----------------Multiplica por 2------------------------------")
print(array_p)
print("----------------Suma 2------------------------------")
print(array_s)
print("----------------resta 2------------------------------")
print(array_r)
print("----------------divide por 2------------------------------")
print(array_d)
#torch.add(), torch.mul(), torch.subtract, torch.div()

array_p = torch.mul(array_pt, 2)
array_s = torch.add(array_pt,2)
array_r = torch.subtract(array_pt,2)
array_d = torch.div(array_pt,2)

print("----------------Multiplica por 2------------------------------")
print(array_p)
print("----------------Suma 2------------------------------")
print(array_s)
print("----------------resta 2------------------------------")
print(array_r)
print("----------------divide por 2------------------------------")
print(array_d)
print("----------------TENSORFLOW------------------------------")

array_tf = tf.Variable([[25,2],[5,26],[3,7]])

#tf.add(), tf.mul(), tf.subtract, tf.div()
array_p = torch.mul(array_tf, 2)
array_s = torch.add(array_tf,2)
array_r = torch.subtract(array_tf,2)
array_d = torch.div(array_tf,2)

print("----------------Multiplica por 2 array_p------------------------------")
print(array_p)
print("----------------Suma 2 array_s------------------------------")
print(array_s)
print("----------------resta 2------------------------------")
print(array_r)
print("----------------divide por 2------------------------------")
print(array_d)

#El producto Hadamard se hace elemento a elemento 
#deben tener el mismo tamano para que se haga este producto
#   x[i] + y[i], x[i] * y[i]
print("----------------Sumamos array_p + array_s------------------------------")
print(array_p + array_s)

print("----------------multiplicamos array_p * array_s------------------------------")
print(array_p * array_s)