#Fecha de creación: 6 de abril de 2026
#Tema: Polinomio de Lagrange
#Autor: Beatriz Almaraz

from sympy import Symbol, simplify, expand, N
x = Symbol('x')

#Forma sin iterar, solo para 3 puntos, se puede usar la 
# función lagrange para n puntos (Se muestra al final)
"""
X0=0; Y0=15/2
X1=3; Y1=7
X2=9; Y2=9/2

L0= ((x-X1)/(X0-X1))*((x-X2)/(X0-X2))
L1= ((x-X0)/(X1-X0))*((x-X2)/(X1-X2))
L2= ((x-X0)/(X2-X0))*((x-X1)/(X2-X1))

print(N(simplify(L0), 6))
print(N(simplify(L1), 6))
print(N(simplify(L2), 6))

print(N(expand(L0), 6))

Px=Y0*L0 + Y1*L1 + Y2*L2
print(N(expand(Px), 6))
"""

print("\nUsando una funcion para un polinomio de n raices\n")

def lagrange(X, Y, Xn):
    n = len(X)
    Yn = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (Xn - X[j]) / (X[i] - X[j])
        Yn = Yn + Y[i] * L
    return Yn

X = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
Y = [0.54, 0.45, 0.36, 0.27, 0.17, 0.07, -0.03, 
     -0.13, -0.23, -0.32, -0.42]

Xn = 0.15
Yn = lagrange(X, Y, Xn)
print(f"El valor de P({Xn}) es: {Yn}")

Xn = 0.63
Yn = lagrange(X, Y, Xn)
print(f"El valor de P({Xn}) es: {Yn}")

"""
Xn = 0
Yn = lagrange(X, Y, Xn)
print(f"El valor de P({Xn}) es: {Yn}")
"""
