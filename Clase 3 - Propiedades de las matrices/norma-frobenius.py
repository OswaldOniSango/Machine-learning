# Norma de Frobenius nos sirve para medir el tamaño de una matriz, es decir, la distancia entre la matriz y la matriz nula. Es útil para comparar matrices y evaluar su magnitud.
import numpy as np
# Definir una matriz A
A = np.array([[1, 2], [3, 4]])
# Calcular la norma de Frobenius de la matriz A
norma_frobenius = np.linalg.norm(A)
print("La norma de Frobenius de la matriz A es:", norma_frobenius)

# La norma de Frobenius se calcula como la raíz cuadrada de la suma de los cuadrados de todos los elementos de la matriz. En este caso, la norma de Frobenius de la matriz A es aproximadamente 5.4772.
matriz = np.array([[1, 2], [3, 4]])
matriz_frobenius = (1**2 + 2**2 + 3**2 + 4**2)**0.5
print("La norma de Frobenius calculada manualmente es:", matriz_frobenius)  

#Pytorch también tiene una función para calcular la norma de Frobenius, que es torch.norm(). Aquí hay un ejemplo de cómo usarla:
import torch
# Definir una matriz A como un tensor de PyTorch
A_torch = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
# Calcular la norma de Frobenius de la matriz A usando PyTorch
norma_frobenius_torch = torch.norm(A_torch)
print("La norma de Frobenius de la matriz A usando PyTorch es:", norma_frobenius_torch.item())

#TensorFlow también tiene una función para calcular la norma de Frobenius, que es tf.norm(). Aquí hay un ejemplo de cómo usarla:
import tensorflow as tf
# Definir una matriz A como un tensor de TensorFlow
A_tf = tf.Variable([[1, 2], [3, 4.]])
# Calcular la norma de Frobenius de la matriz A usando TensorFlow
norma_frobenius_tf = tf.norm(A_tf)
print("La norma de Frobenius de la matriz A usando TensorFlow es:", norma_frobenius_tf.numpy())