import matplotlib.pyplot as plt
import numpy as np

#crea una linea de 0 a 60 con 1000 puntos uniformemente distribuidos
d = np.linspace(0,60,1000)

#Cantidad de enerigia del M1 
m_1 = 1 * d

#Cantidad de energia del M2
m_2 = 4 * (d - 30)

#crea un lienzo y los ejes
fig, ax = plt.subplots()

plt.title('Paneles Solares')
plt.xlabel('tiempo en dias')
plt.ylabel('DEnergia en KJ')

ax.set_xlim([0,60])
ax.set_ylim([0,100])
ax.plot(d, m_1, c='green')
ax.plot(d, m_2, c='red')

plt.axvline(x=40, color = 'blue', linestyle='--')
plt.axhline(y=40, color = 'blue', linestyle='--')



plt.show()

