#Fecha de creación: 27 de marzo de 2026
#Tema: Polinomio Característico
#Autor: Beatriz Almaraz Garcia

from numpy import matrix, eye, zeros, dot, array, poly1d, set_printoptions
set_printoptions(precision=2, floatmode='fixed')

def celda(M,r,c):
    C=M[r,c]
    return C
def renglon(M,r):
    R=M[r,:]
    return R
def columna(M,c):
    C=M[:,c]
    return C 

"""
print('Matriz A\n', A)
print('Matriz Y\n', Y)
print('AY\n', A*Y)
A2= A**2; print(A2)
A3= A**3; print(A3)
print('A3Y\n', A3*Y)
A3Y= A3*Y; print(A3Y)
B= -A3Y; print(B)
print('AY2\n', A2*Y)
AY2= A2*Y; print(AY2)
AY= A*Y; print(AY)
"""

def gaussJordan(A,B):
    from numpy import hstack
    MB=hstack([A,B])
    n=len(MB)
    for p in range(n):
        for c in range(n):
            if (p!=c):
                F=celda(MB,c,p)/celda(MB,p,p)
                MB[c,:]=renglon(MB,c)-F*renglon(MB,p)
    for p in range(n):
        divisor=celda(MB,p,p)
        MB[p,:]=MB[p,:]/divisor
    return MB

def polinomio_caracteristico(A, Y):
    n = len(A)
    B = -A**(n) * Y
    M = zeros((n, n))
    for i in range(n):
        M[:, i:i+1] = A**(n-1-i) * Y
    return B, M

A=matrix([[2, 0, 1], [3, 1, 4], [0, 2, 5]])*1.0
Y=matrix([[1], [0], [0]])*1.0 #vector de prueba

B, M = polinomio_caracteristico(A, Y)
sol = gaussJordan(M, B)
coef = [1] + array(sol[:, -1]).ravel().tolist()
print('Matriz B\n', B)  
print('Matriz M\n', M)
print('Gauss-Jordan de M y B\n', sol)
print('Polinomio Caracteristico\n', poly1d(coef))