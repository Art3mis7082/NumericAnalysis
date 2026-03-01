#Clase: Análisis numérico
#Tema: Graficar con Matplotlib
#Fecha de creación: 23 de febrero de 2026
#Autor: Beatriz Almaraz

import matplotlib.pyplot as plt
from numpy import arange, cos


def graficar(x, y):

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='X', ylabel='Y', title='Titulo')
    ax.grid()
    plt.show()

x = [1, 2, 3, 4, 5]  # Longitud 5
y = [1, 4, 9, 16, 25]  # Longitud 5
graficar(x,y)

x= arange(0, 6, 0.1)
y=x**3
y= cos(x)

graficar(x, y)

