import numpy as np
import torch as torch
import tensorflow as tf


#el producto escalar seria una reducion de productos y suma de elementos
#se hace primero la multiplicacion y luego la reduccion por suma
print("----------------NUMPY------------------------------")

array_npx = np.array([25,2,5])
array_npy = np.array([0,1,2])
#El producto escalar lo calculamos de la siguiente manera
print(20*0 + 2*1 + 5*2)
print(np.dot(array_npx, array_npy))

print("----------------PYTORCH------------------------------")

array_ptx = torch.tensor([25,2,5])
array_pty = torch.tensor([0,1,2])
print(torch.dot(array_ptx, array_pty))

print("----------------TENSORFLOW------------------------------")

array_tfx = tf.Variable([25,2,5])
array_tfy = tf.Variable([0,1,2])

print(tf.reduce_sum(tf.multiply(array_tfx, array_tfy)))
