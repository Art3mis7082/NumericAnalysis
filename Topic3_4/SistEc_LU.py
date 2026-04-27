#Fecha de creación: 23 de marzo de 2026
#Tema: Sistemas de ecuaciones con LU
#Autor: Beatriz Almaraz Garcia

from numpy import matrix, eye, zeros, dot, array, set_printoptions

set_printoptions(precision=5, suppress=True, floatmode='fixed') 

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

def haciaAdelante(L,B):
    n=len(L)
    Y=zeros([n,1])
    for i in range(n):
        suma=0.0
        for j in range(i):
            suma=suma+L[i,j]*Y[j,0]
        Y[i,0]=(Celda(B,i,0)-suma)/Celda(L, i, i)
    return Y

def haciaAtras(U,Y):
    n=len(U)
    X=zeros([n,1])
    for i in range(n-1,-1,-1):
        X[i]=(Celda(Y,i,0)-dot(Renglon(U, i),X))/Celda(U, i, i)
    return X

A=matrix([[1, 3, -4, 3], [7, -8, 3, 2], [1, 3, 4, 5], [0, 2, 1, 7]])*1.0
B=matrix([[-4], [0], [-10], [-19]])*1.0
[L,U]=LU(A)


print('L=\n',L)
print('U=\n',U)
print('LU=\n',L*U)

Y=haciaAdelante(L,B)
print('Y=\n',Y)

X=haciaAtras(U,Y)
print('X=\n',X)
