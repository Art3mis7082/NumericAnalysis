#Fecha de creación: 9 de marzo de 2026
#Tema: Método Gauss-Seidel
#Autor: Beatriz Almaraz García

def GaussSeidel(X0, Y0, Z0, W0, Fx, Fy, Fz, Fw, tol):
    Ex=tol+1; Ey=tol+1; Ez=tol+1; Ew=tol+1; i=1
    
    while (Ex>tol or Ey>tol or Ez>tol or Ew>tol) and (i<1000):
        X1=Fx(Y0,Z0,W0); Ex=abs(X1-X0)

        Y1=Fy(X1,Z0,W0); Ey=abs(Y1-Y0)
        
        Z1=Fz(X1,Y1,W0); Ez=abs(Z1-Z0)

        W1=Fw(X1,Y1,Z1); Ew=abs(W1-W0)

        print("Iteracion: ",i,"\nX0: ",X0,"\nY0: ",Y0,"\nZ0: ",Z0,"\nW0: ",W0,"\nX: ",X1,"\nY: ",Y1,"\nZ: ",Z1,"\nW: ",W1,"\nError X: ",Ex,"\nError Y: ",Ey,"\nError Z: ",Ez,"\nError W: ",Ew)

        i=i+1
        X0=X1; Y0=Y1; Z0=Z1; W0=W1



Fx=lambda y,z,w: (1/10)*(7+4*y-2*z+3*w)
Fy=lambda x,z,w: -(1/8)*(5+2*x-3*z+2*w)
Fz=lambda x,y,w: (1/9)*(-9-x+4*y+3*w)
Fw=lambda x,y,z: -(1/10)*(-29-2*x+2*y+3*z)
x0=0; y0=0; z0=0; w0=0; tol=0.0001
GaussSeidel(x0,y0,z0,w0,Fx,Fy,Fz,Fw,tol)