#Fecha de creación: 20 de abril de 2026
#Tema: Método del trapecio para aproximar la integral de una función
#Autor: Beatriz Almaraz

from numpy import cos, arange


def Trapecio(f,a,b,n):
    h=(b-a)/n
    print("h=",h)
    A1=h*0.5*(f(a)+f(b))
    A2=0
    for i in range(1,n):                        
        A2+=h*f(a+i*h)
    At=A1+A2
    return At

f =lambda x:cos(x)-x
a=1; b=2; n=10
At =Trapecio(f,a,b,n)
print(f"El valor aproximado de la integral es: {At:0.6f}")