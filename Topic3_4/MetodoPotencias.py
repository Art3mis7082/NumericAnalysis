#Fecha de creación: 27 de marzo de 2026
#Tema: Metodo de Potencias
#Autor: Beatriz Almaraz

from numpy.linalg import inv
from numpy import matrix, max, abs

def MaxLambda(A, X0, tol):
    i=1; Ex=tol+1
    L = 0.0
    X1 = X0
    while Ex>tol:
        AX0 = A*X0
        #print('AX0\n', AX0)
        L= max(abs(AX0))
        #print('Lambda\n', L)
        X1 = AX0/L
        #print('X1\n', X1)
        Ex= min(max(abs(X1-X0)), max(abs(X1+X0)))
        print(f"i={i:0.0f}, L={L:0.4f}, Ex={Ex:0.4f}")
        print("X1\n", X1)
        i=i+1
        X0=X1

    return {"lambda": float(L), "iter": i-1, "error": float(Ex), "vector": X1}

    #print(f"i={i:0.0f}, L={L:0.4f}, Ex={Ex:0.4f}")
    #print("X1\n", X1)

def MinLambda(A, X0, tol):
    i=1; Ex=tol+1
    A=inv(A)
    L = 0.0
    X1 = X0
    while Ex>tol:
        AX0 = A*X0
        #print('AX0\n', AX0)
        L= max(abs(AX0))
        #print('Lambda\n', L)
        X1 = AX0/L
        #print('X1\n', X1)
        Ex= min(max(abs(X1-X0)), max(abs(X1+X0)))
        print(f"i={i:0.0f}, L_inv={L:0.4f}, lambda_min={1/L:0.4f}, Ex={Ex:0.4f}")
        print("X1_min\n", X1)
        i=i+1
        X0=X1

    return {"lambda": float(1/L), "iter": i-1, "error": float(Ex), "vector": X1}

A = matrix([[2, 1, 1], [3, 1, 4], [1, 2, 5]])*1.0
X0 = matrix([[0], [1], [0]])*1.0 #Vector inicial
tol = 0.001
res_max = MaxLambda(A, X0, tol)
print("----------------------")
res_min = MinLambda(A, X0, tol)

print("\n========== Resumen ==========")
print(f"Lambda max aprox: {res_max['lambda']:.6f}")
print(f"Iteraciones max: {res_max['iter']}, Error final: {res_max['error']:.6f}")
print(f"Lambda min aprox: {res_min['lambda']:.6f}")
print(f"Iteraciones min: {res_min['iter']}, Error final: {res_min['error']:.6f}")
