#Fecha de creación: 20 de marzo de 2026
#Tema: Sistemas de ecuaciones con LU
#Autor: Beatriz Almaraz Garcia

from numpy import matrix, eye


def Renglon(m,r):
    R=m[r,:]
    return R

def Columna(m,c):
    C=m[:,c]
    return C

def Celda(m,r,c):
    RC=m[r,c]
    return RC

def LU(A):
    n=len(A)
    L=eye(n)
    U=A*1.0

    for P in range(n):
        if Celda(U,P,P) == 0:
            raise ValueError('Pivote cero: se requiere pivoteo parcial.')
        for C in range(P+1,n):
            F= Celda(U,C,P)/Celda(U,P,P)
            print('F=',F)
            U[C,:] = Renglon(U,C)-F*Renglon(U,P)
            L[C,P] = F
    return L,U

A=matrix([[-1, 3, 2], [3, -4, 1], [2, 5, -2]])*1.0
[L,U]=LU(A)


print('L=\n',L)
print('U=\n',U)
print('LU=\n',L*U)


