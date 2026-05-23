#Fecha de creación: 27 de abril de 2026
#Tema: Método de Euler, Taylor y Runge-Kutta orden 2 y 4
#  para resolver ecuaciones diferenciales ordinarias
#Autor: Beatriz Almaraz

#Nota importante: Taylor es más preciso pero 
#   requiere derivadas, mientras que Euler es más 
#   sencillo pero menos preciso.

from numpy import arange, zeros, cos, sin, linspace
import matplotlib.pyplot as plt
import sympy as sp
from numpy import zeros as np_zeros

def Euler(f,a,b,X0,Y0,h):
    n = int(round((b-a)/h))
    k = 0
    p = n + 1
    M = zeros([p,2])
    M[0,0] = X0; M[0,1] = Y0
    print("\nMetodo de Euler :")

    for i in range(1,n+1):
        Y1 = Y0 + h*f(X0)
        k = k + 1
        X1 = X0 + h
        print(f"k= {k:0.0f} x= {X1:0.4f} y= {Y1:0.4f}")
        M[i,0] = X1; M[i,1] = Y1
        X0 = X1; Y0 = Y1

    return M

def EulerMod(f,a,b,X0,Y0,h, graficar=True):
    n = int(round((b-a)/h))
    p = n+1
    M = zeros([p,2])
    M[0,0] = X0; M[0,1] = Y0
    k = 0

    print("\nMetodo de Euler mejorado:")
    
    for i in range(1,p):
        k= k + 1
        Ys = Y0 + h*f(X0)
        Y1 = Y0 + h/2*(f(X0) + f(X0+h))
        X1 = X0 + h
        print(f"k= {k:0.0f} x= {X1:0.4f} y= {Y0:0.4f}")

        M[i,0] = X1; M[i,1] = Y1
        X0 = X1; Y0 = Y1

    return M 

def Taylor(f,a,b,X0,Y0,h):
    x = sp.Symbol('x')
    n = int(round((b-a)/h))
    p = n + 1
    M = np_zeros([p,2])
    M[0,0] = X0; M[0,1] = Y0
    print("\nMetodo de Taylor:")
    
    k = 0
    for i in range(1,p):
        x0 = X0
        F1 = 3*cos(3*x0)-1
        F2 = -9*sin(3*x0)
        F3 = -27*cos(3*x0)
        F4 = 81*sin(3*x0)

        Y1 = Y0 + (h**1/1)*F1 + (h**2/2)*F2 + (h**3/6)*F3 + (h**4/24)*F4
        X1 = X0 + h
        print(f"k= {k:0.0f} x= {X1:0.4f} y= {Y1:0.4f}")
        k = k + 1
        M[i,0] = X1; M[i,1] = Y1
        X0 = X1; Y0 = Y1

    return M

def Runge_Kutta(f,a,b,X0,Y0,h):
    
    n = int(round((b-a)/h))
    k = 0
    p = n + 1
    M = zeros([p,2])
    M[0,0] = X0; M[0,1] = Y0
    print("\nMetodo de Runge-Kutta orden 2:")
    
    print(f"k= {k:0.0f} x= {a:0.4f} y= {Y0:0.4f}")

    for i in range(1,n+1):
        try:
            k1 = f(X0, Y0)
            k2 = f(X0 + h/2, Y0 + (h/2)*k1)
        except TypeError:
            k1 = f(X0)
            k2 = f(X0 + h/2)

        Y1 = Y0 + h*k2
        X1 = X0 + h
        print(f"k= {k:0.0f} x= {X1:0.4f} y= {Y1:0.4f}")
        k = k + 1
        M[i,0] = X1; M[i,1] = Y1
        X0 = X1; Y0 = Y1

    return M

def Runge_Kutta4(f,a,b,X0,Y0,h):
    n = int(round((b-a)/h))
    k = 0
    p = n + 1
    M = zeros([p,2])
    M[0,0] = X0; M[0,1] = Y0
    print("\nMetodo de Runge-Kutta orden 4:")

    for i in range(1, n+1):
        try:
            k1 = f(X0, Y0)
            k2 = f(X0 + h/2, Y0 + (h/2)*k1)
            k3 = f(X0 + h/2, Y0 + (h/2)*k2)
            k4 = f(X0 + h, Y0 + h*k3)
        except TypeError:
            k1 = f(X0)
            k2 = f(X0 + h/2)
            k3 = f(X0 + h/2)
            k4 = f(X0 + h)

        Y1 = Y0 + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        X1 = X0 + h
        print(f"k= {k:0.0f} x= {X1:0.4f} y= {Y1:0.4f}")
        k = k + 1
        M[i,0] = X1; M[i,1] = Y1
        X0 = X1; Y0 = Y1

    return M

def ComparaTres(f_lambda, f_sym, a, b, X0, Y0, h):

    #MEuler = Euler(f_lambda, a, b, X0, Y0, h)
    #MEulerMod = EulerMod(f_lambda, a, b, X0, Y0, h, graficar=False)
    #MTaylor = Taylor(f_sym, a, b, X0, Y0, h)
    MR_Kutta2 = Runge_Kutta(f_lambda, a, b, X0, Y0, h)
    MR_Kutta4 = Runge_Kutta4(f_lambda, a, b, X0, Y0, h)

    plt.figure(figsize=(10, 6))
    #plt.plot(MEuler[:,0], MEuler[:,1], marker='o', label='Euler', markersize=4, alpha=0.75)
    #plt.plot(MEulerMod[:,0], MEulerMod[:,1], marker='s', label='Euler mejorado', markersize=4, alpha=0.75)
    #plt.plot(MTaylor[:,0], MTaylor[:,1], marker='^', label='Taylor', markersize=4, alpha=0.75)
    plt.plot(MR_Kutta2[:,0], MR_Kutta2[:,1], marker='d', label='Runge-Kutta 2', markersize=4, alpha=0.75)
    plt.plot(MR_Kutta4[:,0], MR_Kutta4[:,1], marker='x', label='Runge-Kutta 4', markersize=4, alpha=0.75)
    plt.title('Método de Runge-Kutta orden 2 y 4 para resolver EDO')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

    return MR_Kutta2, MR_Kutta4, #Euler, MEulerMod, MTaylor

f = lambda x: 3*cos(3*x)-1
f_sym = None
a = 0; b = 8
X0 = 0; Y0 = 3
h = 0.75

print("\n=== Comparacion de los metodos ===")
ComparaTres(f, f_sym, a, b, X0, Y0, h)
