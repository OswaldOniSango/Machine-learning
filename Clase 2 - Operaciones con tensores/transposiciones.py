import numpy as np
import torch as pt
import tensorflow as tf

print("----------------NUMPY------------------------------")

array_np = np.array([[25,2],[5,26],[3,7]])
print(array_np)

array_T = array_np.T
print(array_T)


print("----------------PYTORCH------------------------------")

array_pt = pt.tensor([[25,2],[5,26],[3,7]])
print(array_pt)

array_T = array_pt.T
print(array_T)

print("----------------TENSORFLOW------------------------------")

array_tf = tf.Variable([[25,2],[5,26],[3,7]])
print(array_tf)

array_T = tf.transpose(array_tf)
print(array_T)

