#Clase: Análisis Numérico
#Tema: Metodo cerrado. Método de Secante
#Fecha de creación: 16 de febrero de 2026

from numpy import cos

def secante(Xa, Xb, f, Tolerancia):
    i=1 #Contar el numero de iteraciones
    Emax=Tolerancia+1   #Error máximo

    Ya=f(Xa) #Evaluar en el punto propuesto
    Yb=f(Xb) #Evaluar en el punto propuesto

    while Emax>=Tolerancia:

        Xc= Xb - (Yb*(Xb-Xa))/(Yb-Ya) #Secante
        Yc=f(Xc) 

        print("Iteracion: ",i," Xa: ", f"{Xa:0.4f}","\n Xb: ", Xb,"\n Xc: ", f"{Xc:0.4f}","\n f(Xa): ",f"{Ya:0.4f}","\n f(Xb): ",f"{Yb:0.4f}","\n f(Xc): ",f"{Yc:0.4f}", "\n Error: ",Emax,"\n")

        if Ya*Yc<0:
            Xb=Xc
            Yb=Yc
        else:
            Xa=Xc
            Ya=Yc

        Emax=abs(Yc)
        i+=1

f = lambda x: cos(x)-x

Tolerancia=0.001 #Tolerancia propuesta

Xa=0.0 #Propuesto
Xb=2.0 #Propuesto

secante(Xa,Xb,f,Tolerancia)