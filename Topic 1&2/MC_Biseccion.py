#Clase: Análisis Numérico
#Tema: Metodo cerrado. Método de Bisección
#Fecha de creación: 16 de febrero de 2026

from numpy import cos

def bisección(Xa,Xb,f,Tolerancia):
    i=1 #Contar el numero de iteraciones
    Emax=Tolerancia+1   #Error máximo

    while Emax>=Tolerancia:
        Xc=(Xa+Xb)/2.0 #Punto medio

        Ya=f(Xa) #Evaluar en el punto propuesto
        Yb=f(Xb) 
        Yc=f(Xc) 

        print("Iteracion: ",i," Xa: ",f"{Xa:0.4}","\n Xb: ", Xb," Xc: ",Xc,"\n f(Xa): ",Ya,"\n f(Xb): ",Yb,"\n f(Xc): ",Yc, "\n Error: ",Emax,"\n")

        if Ya*Yc<0:
            Xb=Xc
        else:
            Xa=Xc

        Emax=abs(Yc)
        i+=1

f = lambda x: cos(x)-x
i=1 #Contar el numero de iteraciones

Tolerancia=0.001 #Tolerancia 

Xa=0.0 #Propuesto
Xb=2.0 #Propuesto

bisección(Xa,Xb,f,Tolerancia)