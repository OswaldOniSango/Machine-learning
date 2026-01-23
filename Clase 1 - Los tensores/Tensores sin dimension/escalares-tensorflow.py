
import tensorflow as tf

x_tf = tf.Variable(25, dtype=tf.int16)
y_tf = tf.Variable(3, dtype=tf.int16) # dtype es opcional
print(x_tf)
print(x_tf.shape)
print(y_tf)
print(y_tf.shape)

#suma
print(x_tf + y_tf)
tf_sum = tf.add(x_tf, y_tf)
print(tf_sum)
tf_sum.numpy() # veamos que las operaciones NumPy convierten automáticamente los tensores en matrices NumPy, y viceversa
print(type(tf_sum.numpy()))

#cambiar tipo de dato a float
tf_float = tf.Variable(25., dtype=tf.float16)
print(tf_float)



