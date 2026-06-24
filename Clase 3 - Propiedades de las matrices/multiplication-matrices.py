import numpy as np
import torch 
import tensorflow as tf


# Definir dos matrices A y B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Calcular el producto de las matrices A y B
C = np.dot(A, B)
print("El producto de las matrices A y B es:\n", C)

# Calcular el producto de las matrices A y B usando PyTorch
A_torch = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
B_torch = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
C_torch = torch.matmul(A_torch, B_torch)
print("El producto de las matrices A y B usando PyTorch es:\n", C_torch)

# Calcular el producto de las matrices A y B usando TensorFlow
A_tf = tf.Variable([[1, 2], [3, 4.]])
B_tf = tf.Variable([[5, 6], [7, 8.]])
C_tf = tf.matmul(A_tf, B_tf)
print("El producto de las matrices A y B usando TensorFlow es:\n", C_tf.numpy())