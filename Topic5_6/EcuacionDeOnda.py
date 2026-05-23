#Fecha de creación: 22 de mayo de 2026
#Tema: Ecuación de onda
#Autor: Beatriz Almaraz

from numpy import arange, zeros, linspace, sin, cos, transpose, set_printoptions
import matplotlib.pyplot as plt
from math import pi

def graficaOnda(U):
    R=U.shape[0]
    C=U.shape[1]
    X=arange(R)
    print(X)
    for y  in range(C):
        plt.plot(X,U[:,y])
    plt.show()

def llenarU2(nx,nc):
    U=zeros((nx,nc))
    x=linspace(0,4*pi,nx);
    L=0.25
    t=0.1
    y=L*t*(cos(x)-1);
    U[:,0]=transpose(y);
    return U

def llenarU(nx,nc):
  U=zeros((nx,nc))
  x=linspace(0,10*pi,nx);
  y=zeros(nx);
  L=0.25
  t=0.1
  for  X in range(nx):
    if X<=nx/2:
        y[X]=X/(nx/2)
    else:
        y[X]=(10-X)/(nx/2)
  U[:,0]=transpose(y);
  return U

def EDOOnda(U,L):
  R=U.shape[0]
  C=U.shape[1]

  for x in range(1,R-1):
    for t in range(0,C-1):
        U[x,t+1]=U[x,t]+L/2*(U[x+1,t]-2*U[x,t]+U[x-1,t]);
    
  return U

set_printoptions(suppress=True,precision=4,linewidth=200,floatmode='fixed')
U=llenarU(10,25)
L=0.5
Un=EDOOnda(U,L)
print('Solución:')
print(Un)
graficaOnda(Un)

