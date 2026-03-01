#Fecha de creación: 9 de febrero de 2026
#Tema: Aproximación sucesiva
#Autor: Beatriz Almaraz


#def suma(a,b):
#  s =a+b
#  return s
    
#s=suma(3,4)
#print(f"la suma es {s}")


from numpy import exp
f = lambda x:exp(x)
g = lambda x:1/x

n = [0.57, 0.55, 0.565]

for i in n:
    F=f(i); G=g(i); E=abs(F-G)

    print(f"X= {i:0.6f}  f(x)={F:0.4}  g(x)={G:0.6f}  error={E:0.4f}")
  

#f(x)=exp(x)   g(x)=1/x

