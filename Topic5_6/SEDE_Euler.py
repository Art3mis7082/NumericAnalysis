#fecha de creación: 2026-05-26
#Autor: Beatriz Almaraz
#Tema: Sistema de Ecuaciones Diferenciales, con método de Euler.

from numpy import arange, zeros, cos, sin, linspace
import matplotlib.pyplot as plt
import sympy as sp
from numpy import zeros as np_zeros

def SEDE_Euler(f1,f2,a,b,X0,Y0,Z0,h):
    n = int(round((b - X0)/h))
    p = n + 1
    k = 0
    M = zeros([p,3])
    M[0,0] = X0; M[0,1] = Y0; M[0,2] = Z0;

    print(f"k= {k:0.0f} x= {X0:0.6f} y= {Y0:0.6f} z= {Z0:0.6f}")

    for i in range(1,n+1):
        Y1 = Y0 + h*f1(X0,Y0,Z0)
        Z1 = Z0 + h*f2(X0,Y0,Z0)
        k = k + 1
        X1 = X0 + h
        print(f"k= {k:0.0f} x= {X1:0.6f} y= {Y1:0.6f} z= {Z1:0.6f}")
        M[i,0] = X1; M[i,1] = Y1; M[i,2] = Z1
        X0 = X1; Y0 = Y1; Z0 = Z1

    return M


def plot_SEDE_solution(M, labels=('y','z'), title='Solución — Euler (sistemas)', figsize=(10,6), show=True, save_path=None):
    try:
        x = M[:, 0]
        y = M[:, 1]
        z = M[:, 2]
    except Exception:
        raise ValueError('La matriz M debe tener forma (n,3) con columnas [x,y,z]')

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(x, y, marker='o', linestyle='-', label=labels[0])
    ax.plot(x, z, marker='s', linestyle='--', label=labels[1])
    ax.set_xlabel('x')
    ax.set_ylabel('y, z')
    ax.set_title(title)
    ax.grid(True)
    ax.legend()

    if save_path:
        fig.savefig(save_path, bbox_inches='tight')
    if show:
        plt.show()
    return fig, ax

def f1(x, y, z):
    return x

def f2(x, y, z):
    return x

a = 1; b = 2; X0 = 0; Y0 = 0; Z0 = 0; h = 0.1
print("\n=== Metodo de Euler para sistemas de ecuaciones diferenciales ordinarias ===")
Mse = SEDE_Euler(f1, f2, a, b, X0, Y0, Z0, h)
# Graficar resultado usando la nueva función

#for i in range(len(Mse)):
#    print(f"x= {Mse[i,0]:0.0f} y= {Mse[i,1]:0.0f} z= {Mse[i,2]:0.0f}")

try:
    plot_SEDE_solution(Mse, labels=('y','z'), title='Sistema: Euler')
except Exception as e:
    print('Error al graficar:', e)