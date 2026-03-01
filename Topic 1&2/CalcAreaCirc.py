#Fecha de creación: 6 de febrero de 2026
#Tema: Cálculo de área con su error relativo porcentual
#Autor: Beatriz Almaraz

from math import pi, sin, cos
AC= lambda r: pi*r**2

L=100; r=1

base=2*r*sin(pi/L)
altura=r*cos(pi/L)
AP=L*base*altura/2

print(f"Area1={AC(r)}")
print(f"Area poligono={AP}")

ERP= abs(((AC(r)-AP)/AC(r))*100)
print(f"Error relativo porcentual={ERP:0.4f} %")