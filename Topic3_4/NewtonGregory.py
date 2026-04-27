#Fecha de creación: 10 de abril de 2026
#Tema: Newton Gregory
#Autor: Beatriz Almaraz

from math import cos

h = 0.2
x = 0.13; x0=0; y0=1
s = (x-x0)/h
print(s)
Vd = [-0.0199, -0.0391, 0.0024, 0.0015, -0.0002]

Px= y0 + s*Vd[0] + (s*(s-1)/2)*Vd[1] + (s*(s-1)*(s-2)/6)*Vd[2] + (s*(s-1)*(s-2)*(s-3)/24)*Vd[3] + (s*(s-1)*(s-2)*(s-3)*(s-4)/120)*Vd[4]
print(f"Para x={x:0.4f}, el valor de P(x) es: {Px:0.4f}")

ERP= ((cos(x)-Px)/cos(x))*100
print(f"El error porcentual relativo es: {ERP:0.4f}%")

#-----------
x = 0.5; x0=0.4; y0=0.9211
s = (x-x0)/h
print(s)
Vd = [-0.0957, -0.0329,	0.0051]

Px= y0 + s*Vd[0] + (s*(s-1)/2)*Vd[1] + (s*(s-1)*(s-2)/6)*Vd[2] 
print(f"Para x={x:0.4f}, el valor de P(x) es: {Px:0.4f}")

ERP= ((cos(x)-Px)/cos(x))*100
print(f"El error porcentual relativo es: {ERP:0.4f}%")