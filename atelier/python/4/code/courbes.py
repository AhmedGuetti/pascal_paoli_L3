import matplotlib.pyplot as plt
import numpy as np
#Ici on décrit les abscisses
#Entre 0 et 5 en 10 points
x_axis_list = np.arange(10, 500, 5000, 50000, 100000)
fig, ax = plt.subplots()
#Dessin des courbes, le premier paramètre
#correspond aux point d'abscisse le
#deuxième correspond aux points d'ordonnées
#le troisième paramètre, optionnel permet de
#choisir éventuellement la couleur et le marqueur
ax.plot(x_axis_list,x_axis_list,'bo-',label='Identité')
ax.plot(x_axis_list,x_axis_list**2, 'r*-', label='Carré')
ax.plot(x_axis_list,x_axis_list**3,'g*-', label='Cube')
ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',
title='Fonctions identité, cube et carré')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#fig.savefig("test.png")
plt.show()