#Fecha de creación: 18 de mayo de 2026
#Tema: Método del artillero para resolver ecuaciones diferenciales ordinarias 
#Autor: Beatriz Almaraz

from numpy import zeros

def Artillero(f,a,b,h,y0,y1):
    n = int((b - a) / h)
    p = n+1
    M = zeros([p,2])
    M[0,0] = a; M[1,0] = a+h
    M[0,1] = y0; M[1,1] = y1

    for i in range(2, p):
        M[i,0] = a + i*h
        x = M[i-1, 0]
        y = M[i-1, 1]
        M[i,1] = f(y0, y1, x, y)
        y0 = y1; y1 = M[i,1]
    return M


f = lambda y0, y1, x, y: 18*x*h**2+2*y1-y0
a = 0; b = 1; h = 0.2; y0 = 0; y1 = -0.375 #y1 es el valor variable, tenemos que aproximarnos a 1
M = Artillero(f, a, b, h, y0, y1)
print("x\t\t\t\t\t\t\t\ty")
for i in range(len(M)):
    print(f"{M[i,0]:.1f}\t\t\t\t\t\t{M[i,1]:.6f}")