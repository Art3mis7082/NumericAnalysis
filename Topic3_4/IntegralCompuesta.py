#Fecha de creación: 24 de abril de 2026
#Tema: Integral Compuesta
#Autor: Beatriz Almaraz

from numpy import arange

def TrapecioP(y,h):
    n = len(y)-1
    A1 = h/2*(y[0]+y[-1])
    A2 = 0
    for i in arange(1,n):
        A2 += h*y[i]
    A = A1+A2
    return A

def SimpsonP1_3(y,h):
    n = len(y)-1
    A1 = h*1*1/3*(y[0]+y[-1])
    A2 = 0; A3=0
    for i in arange(1,n,2):
        A2 += h*1*1/3*4*y[i]
    for i in arange(2,n,2):
        A3 += h*1*1/3*2*y[i]
    A = A1+A2+A3
    return A

def SimpsonP3_8(y,h):
    n = len(y)-1
    A1 = h*3*1/8*(y[0]+y[-1])
    A2 = 0; A3=0; A4=0
    for i in arange(1,n,2):
        A2 += h*3*1/8*3*y[i]
    for i in arange(2,n,2):
        A3 += h*3*1/8*3*y[i]
    for i in arange(3,n,3):
        A4 += h*3*1/8*2*y[i]
    A = A1+A2+A3+A4
    return A



y = [1.0000, 1.7280, 2.7440, 3.3750, 5.8320, 9.2610, 13.8240]

y1 = [1.0000, 1.7280, 2.7440]
y2 = [2.7440, 3.3750]
y3 = [3.3750, 5.8320, 9.2610, 13.8240]

h1=0.2 ; h2=0.1 ; h3=0.3
A1 = SimpsonP1_3(y1,h1)
print( "El area 1 es: ", A1)
A2 = TrapecioP(y2,h2)
print( "El area 2 es: ", A2)
A3 = SimpsonP3_8(y3,h3)   
print( "El area 3 es: ", A3)
print( "El area total es: ", A1+A2+A3)

print( "\n--------")

AE1 = TrapecioP(y1,h1)
print( "El Area de trapecio 1 es: ", AE1)
AE2 = TrapecioP(y2,h2)
print( "El Area de trapecio 2 es: ", AE2)
AE3 = TrapecioP(y3,h3)
print( "El Area de trapecio 3 es: ", AE3)
print( "El Area total es: ", AE1+AE2+AE3)

print( "\n--------")
ERP_AT = abs((A1+A2+A3)-(AE1+AE2+AE3))/(A1+A2+A3)*100
print( "El error relativo porcentual es: ", ERP_AT, "%")