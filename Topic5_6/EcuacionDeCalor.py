#Fecha de creación: 22 de mayo de 2026
#Tema: Ecuación de calor
#Autor: Beatriz Almaraz

from numpy import  set_printoptions, zeros, max, arange
import matplotlib.pyplot as plt

def llenarU():
  U=zeros((30,25))
  U[:,0]=30
  U[0,:]=100
  U[-1,:]=70
  return U

def EDOCalor(U,L):
  Ua=U*1.0
  Un=U*1.0
  R=Ua.shape[0]
  C=Ua.shape[1]

  for x in range(1,R-1):
    for t in range(0,C-1):
      U[x,t+1]=U[x,t]+L*(U[x+1,t]-2*U[x,t]+U[x-1,t]);

  return U

def graficaCalor(U):
    R=U.shape[0]; C=U.shape[1];
    X=arange(R)
    print(X)
    for y  in range(C):
        plt.plot(X,U[:,y])
    plt.show()

set_printoptions(suppress=True,precision=4,linewidth=200,floatmode='fixed')
U=llenarU()
print("Matriz inicial:")
print(U)
L=0.15
Un=EDOCalor(U,L)
print('Solución:')
print(Un)
graficaCalor(Un)