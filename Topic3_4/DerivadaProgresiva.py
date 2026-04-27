#Fecha de creación: 17 de abril de 2026
#Tema: Derivadas Progresivas
#Autor: Almaraz Garcia Beatriz

from numpy import cos

def D1p(f, X0, h):
    D1 = (f(X0+h)-f(X0))/h
    return D1

def D1p2o(f, X0, h):
    D1 = (-1*f(X0+2*h)+4*f(X0+h)-3*f(X0))/(2*h)
    return D1

def D2p(f, X0, h):
    D2 = (f(X0+2*h)-2*f(X0+h)+f(X0))/h**2
    return D2

def D3p(f, X0, h):
    D3 = (f(X0+3*h)-3*f(X0+2*h)+3*f(X0+h)-f(X0))/h**3
    return D3


f = lambda x:cos(x)
X0 = 1; h = 0.001; 
D1 = D1p(f, X0, h)
print(f"Primera derivada progresiva ={D1:0.6f}")

D1_2o = D1p2o(f, X0, h)
print(f"Primera derivada progresiva de orden 2 ={D1_2o:0.6f}")
D2 = D2p(f, X0, h)
print(f"Segunda derivada progresiva ={D2:0.6f}")
D3 = D3p(f, X0, h)
print(f"Tercera derivada progresiva ={D3:0.6f}")