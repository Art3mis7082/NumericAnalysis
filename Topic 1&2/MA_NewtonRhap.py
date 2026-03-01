#Fecha de creación: 20 de febrero de 2026
#Tema: Método de Newton-Raphson
#Autor: Beatriz Almaraz

def NR(X0, f, Df, tol):
    i=1 #Contar el numero de iteraciones
    Emax=tol+1   #Error máximo

    while Emax>=tol:
        X1=X0-f(X0)/Df(X0) #Evaluar en el punto propuesto
        VDf=abs(Df(X0)) #Evaluar la derivada en el punto propuesto
        Emax=abs(X1-X0) #Calcular el error
        print("Iteracion: ",i,"\n X0: ",f"{X0:0.5f}","\n X1: ",f"{X1:0.5f}","\n f(X0): ",f"{f(X0):0.5f}"," Df(X0): ",f"{Df(X0):0.5f}"," Error: ",f"{Emax:0.5f}")
        i=i+1
        X0=X1 #Actualizar el punto propuesto

from numpy import cos, sin
#f(x)=4*x-cos(x)
f=lambda x: 4*x-cos(x); Df=lambda x: 4+sin(x)
X0=3 
tol=0.001

NR(X0, f, Df, tol)