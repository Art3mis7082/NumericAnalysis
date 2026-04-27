#Fecha de creación: 20 de abril de 2026
#Tema: Método de simpson 1/3 para aproximar el 
#   valor de una integral definida
#Autor: Beatriz Almaraz

def Simpson1_3(f,a,b,n):
    h=(b-a)/n
    print("h=",h)
    A1=h/3*1*(f(a)+f(b))
    A2=0; A3=0
    for i in range(1,n,2):                        
        A2+=h/3*4*f(a+i*h)
    for i in range(2,n,2):
        A3+=h/3*2*f(a+i*h)
    At=A1+A2+A3
    return At

# Problema: integral de 0 a 1 de x/((x+1)(x+2)) con n=8
f = lambda x: x/((x+1)*(x+2))
a = 0; b = 1; n = 8
At =Simpson1_3(f,a,b,n)
print(f"El valor aproximado de la integral es: {At:0.6f}")