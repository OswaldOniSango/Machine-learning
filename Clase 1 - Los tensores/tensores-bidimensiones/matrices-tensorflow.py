import tensorflow as tf

X_tf = tf.Variable([[25,2],[5,26],[3,7]])

print(X_tf)

#numpy=2 es que se trata de un array bidimensional
print(tf.rank(X_tf))

#el shape que es 3x2
print(tf.shape(X_tf))

print(X_tf[1,:])