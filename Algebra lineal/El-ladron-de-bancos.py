import matplotlib.pyplot as plt
import numpy as np

#crea una linea de 0 a 40 con 1000 puntos uniformemente distribuidos

t = np.linspace(0,40,1000)

#Distancia del ladron, esto es una recta con una pendiente de 2.5
d_r = 2.5 * t

#Distancia del sheriff,
d_s = 3 * (t - 5)

#crea un lienzo y los ejes
fig, ax = plt.subplots()

plt.title('El ladron de bancos atrapado')
plt.xlabel('tiempo en minutos')
plt.ylabel('Distancia en KM')

ax.set_xlim([0,40])
ax.set_ylim([0,100])
ax.plot(t, d_r, c='green')
ax.plot(t, d_s, c='red')

plt.axvline(x=30, color='purple', linestyle='--')
plt.axhline(y=75, color='purple', linestyle='--')

plt.show()

