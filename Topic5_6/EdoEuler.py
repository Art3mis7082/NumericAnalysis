#Fecha de creación: 17 de mayo de 2026
#Tema: Ecuaciones diferenciales ordinarias de tercer orden. Método de Euler.
#Autor: Beatriz Almaraz

from math import cos
import matplotlib.pyplot as plt

def EdoEulerTercerOrden(a, b, n, y0, z0, w0):
    # z = y' y w = y''
    # y''' = -cos(x) - 6
    h = (b - a) / n
    x = a; y = y0; z = z0; w = w0
    xs = []
    ys = []

    for k in range(n + 1):
        print(f"K={k:2d}  x={x:0.4f}  y={y:9.5f}  z={z:9.5f}  w={w:9.5f}")
        xs.append(x)
        ys.append(y)

        y1 = y + h * z
        z1 = z + h * w
        w1 = w + h * (-cos(x) - 6)

        x = x + h
        y = y1
        z = z1
        w = w1

    return xs, ys

def GraficarEuler(xs, ys):
    plt.plot(xs, ys, marker='o', color='teal', label='Euler (y)')
    plt.title('EDO de tercer orden con Euler')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

a = 0; b = 1
n = 10
y0 = -6; z0 = 1; w0 = 0

xs, ys = EdoEulerTercerOrden(a, b, n, y0, z0, w0)
GraficarEuler(xs, ys)