# Matriz diagonal es cuando tienes elementos no nulos a lo largo de la diagonal principal, ceros en todas las demas partes
#una matriz de identidad es un ejemplo de matriz diagonal, se denora diag(x).
#son muy eficiente.
import numpy as np
# Definir una matriz diagonal D
D = np.diag([1, 2, 3])
print("La matriz diagonal D es:\n", D)