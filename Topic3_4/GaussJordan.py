#Fecha de creación: 6 de marzo de 2026
#Tema: Gauss Jordan
#Autor: Beatriz Almaraz Garcia

def celda(M,r,c):
    C=M[r,c]
    return C
def renglon(M,r):
    R=M[r,:]
    return R
def columna(M,c):
    C=M[:,c]
    return C
def formato_matrices():
    from numpy import set_printoptions
    set_printoptions(precision=4,suppress=True)

def imprimir_solucion(X):
    n=len(X)
    print("Solucion de cada incognita:")
    for i in range(n):
        print(f"x{i+1} = {float(X[i,0]):.4f}")

def GaussJordanPivoteoTotal(M,B):
    n=len(M)
    MB=hstack([M,B])*1.0
    marcas=list(range(n))

    for p in range(n):
        max_f=p
        max_c=p
        max_val=abs(celda(MB,p,p))
        for f in range(p,n):
            for c in range(p,n):
                valor=abs(celda(MB,f,c))
                if valor>max_val:
                    max_val=valor
                    max_f=f
                    max_c=c

        if max_val==0:
            raise ValueError("El sistema no tiene pivote valido (matriz singular).")

        if max_f!=p:
            temp=renglon(MB,p).copy()
            MB[p,:]=renglon(MB,max_f)
            MB[max_f,:]=temp

        if max_c!=p:
            temp=columna(MB,p).copy()
            MB[:,p]=columna(MB,max_c)
            MB[:,max_c]=temp
            marcas[p],marcas[max_c]=marcas[max_c],marcas[p]

        for f in range(n):
            if f!=p:
                F=celda(MB,f,p)/celda(MB,p,p)
                MB[f,:]=renglon(MB,f)-F*renglon(MB,p)

    x_temp=matrix([[0.0] for _ in range(n)])
    for i in range(n):
        x_temp[i,0]=celda(MB,i,n)/celda(MB,i,i)

    x=matrix([[0.0] for _ in range(n)])
    for i in range(n):
        x[marcas[i],0]=x_temp[i,0]

    return MB,x

from numpy import matrix,hstack
M=matrix([[1,3,-4,3],[7, -8, 3, 2],[1, 3, 4, 5], [0, 2, 1, 7]])*1.0
B=matrix([[-4],[0],[-10], [-19]])*1.0
MB_inicial=hstack([M,B])

print("--------")
print("Matriz M:")
print(M)
print("--------")
print("Vector B:")
print(B)
print("--------")
print("Sistema expandido [M|B]:")
print(MB_inicial)

MB,X=GaussJordanPivoteoTotal(M,B)

print("--------")
formato_matrices()
print("Solucion X:")
imprimir_solucion(X)