#Fecha de creación: 20 de abril de 2026
#Tema: Método de simpson 3/8 para aproximar el 
#   valor de una integral definida
#Autor: Beatriz Almaraz

from numpy import cos


def Simpson3_8(f,a,b,n):
    h=(b-a)/n
    print("h=",h)
    A1=3*h/8*(f(a)+f(b))
    A2=0
    A3=0
    for i in range(1,n):
        if i % 3 == 0:
            A3 += 2*f(a+i*h)
        else:
            A2 += 3*f(a+i*h)

    At=A1+3*h/8*(A2+A3)
    return At

f =lambda x:x/((x+1)*(x+2))
a=0; b=1; n=9
At =Simpson3_8(f,a,b,n)
print(f"El valor aproximado de la integral es: {At:0.6f}")