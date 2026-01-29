#un vector puede representar un punto en el espacio, tambien podemos pensar que 
#que se puede representar una magnitud, que tan larga es la fecha que va del punto 
#[0,0] al punto [x,x]. Es decir, los vecores representan una magnirut y una direccino
#a partir del origen

#por esto existen las normas, que son funciones que cuantifican la magnitud de los
#veectores

#Nomal L2, se describe como la raiz cuadrada de la sumatioria de x sub i al cuadrado
#esto mide la distancia dismple (euclideana) desde el origen,
#esta es la norma mas comun en aprendizaje automatico
#se denota ||x||2

import numpy as np

array = np.array([25, 2, 5])

print(array)

#la norma seria la raiz cuadrada de la sumatioria de x sub i al cuadrado
norma = (25**2 + 2**2 + 5**2)**(1/2)
print(norma)

#como todo siempre hay un metodo para ello en linald (algebra lineal)
norma_f = np.linalg.norm(array)
print(norma_f)

#si el espacio vectorial tridimensional donde vivia este vector
#esta expresado en metros entonces la longitud seria 25,6 metros 


#norma de L cuadrado al cuadrado
#esta es computacionalmente menos costasa que usar la nomre L2 ya que
#*La norma l2 al cuadrado es simplemente el producto xT multiplicado x (es muy rapido)
#*La derivada del elemento x requiere ese lemento solo, mientras que la norma L2 requiere el vector x
#INCONVENIENTE: crece lentamente cerca del origen, por lo que no puede utilizarse si es importante
#distinguier entre cero y casi cero
norma_cuadrado = (25**2 + 2**2 + 5**2)
print(norma_cuadrado)
np.dot(array, array)

#Norma del maximo
norma_maximo = np.max([np.abs(25), np.abs(2), np.abs(5) ])
print(norma_maximo)

