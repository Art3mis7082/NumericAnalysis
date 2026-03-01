#Fecha de creación: 27 de febrero de 2026
#Tema: Método de factores de cuadraticos 
#Nombre: Almaraz García Beatriz

def fact2(a, tol):

    from numpy import zeros
    
    n= len(a)-1; print(n)
    Er=tol+1; Es=tol+1; i=1
    
    P=0; Q=0; k=n-2

    B=zeros(n+3); print(B)
    while (Er>=tol and Es>=tol):
        for k in range(k+1):
        #print(j)
            B[k]=a[k]-P*B[k-1]-Q*B[k-2]
        R=a[n-1]-P*B[n-2]-Q*B[n-3]
        S=a[n]-Q*B[n-2]
        P=R/B[n-2]+P
        Q=S/B[n-2]+Q
        i=i+1; Er=abs(R); Es=abs(S);  
        print("Iteración: ", i)
        print("Polinomio solución: ", B[0:n-1])
        print("Polinomio residual: ", R, S)

    
    B=B[0:-2]
    print("\ni=", i, "\nP=", P, "\nQ=", Q, "\nB=", B)
    return B, P, Q    
    
#x**6+2*x**5-68*x**4-70*x**3+739*x**2+68*x**1-672    
a=[1, 2, -68, -70, 739, 68, -672]
tol=0.001
fact2(a, tol)