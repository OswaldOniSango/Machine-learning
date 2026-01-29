#Bases de vectores, son un conjunto de vectores que puedes escalaese para respresentar cualquier vector
#en un espacion vectorial determinado

#Puedes ver las bases de vectores como en el eje de las x va de (0,1) 
#y en el eje de las y va de (1,0)

#Vectores Ortogonales
#si realizamos el producto escalar(dot) de dos vectores ortogonales el resultado es cero
#si tienen norma diferentes de 0 (longitud != 0)forman un angulo de 90 grados
#Ortogonal significa perpendicular
#si tenemos n dimiensiones hay como mucho n vectores mutualmente ortogonales (asumiento que longitud != 0)
#
# 
# Vectores Ortonormales
# son ortogonales y tienen norma unitaria, son ortonormales y tienen norma = 1.
import numpy as np

x = np.array([1,0])  

y = np.array([0,1])  

dot_result = np.dot(x,y)

#Resultado debe ser cero
print(dot_result)