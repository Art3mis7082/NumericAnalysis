#Fecha de creación: 20 de febrero de 2026
#Tema: Aproximación sucesiva
#Autor: Beatriz Almaraz

def AproxSus(X0, g, Dg, tol):
    i=1 #Contar el numero de iteraciones
    Emax=tol+1   #Error máximo
    X1=X0  #Inicializar X1

    while Emax>=tol:
        X1=g(X0) #Evaluar en el punto propuesto
        VDg=abs(Dg(X0)) #Evaluar la derivada en el punto propuesto
        Emax=abs(X1-X0) #Calcular el error
        print("Iteracion: ",i,"\n X0: ",f"{X0:0.4f}","\n X1: ",f"{X1:0.4f}","\n g(X0): ",f"{g(X0):0.4f}"," Dg(X0): ",f"{Dg(X0):0.4f}"," Error: ",f"{Emax:0.4f}")
        i=i+1
        X0=X1 #Actualizar el punto propuesto
    
    print("La aproximación es: ",f"{X1:0.4f}"," con un error de: ",f"{Emax:0.4f}"," y se realizaron ",i-1," iteraciones.")


from numpy import cos, sin
#f(x)=4*x-cos(x)
g=lambda x: (cos(x)/4); Dg=lambda x: -sin(x)/4
X0=0.5 #Valor inicial propuesto
tol=0.001 #Tolerancia solicitada

AproxSus(X0, g, Dg, tol)