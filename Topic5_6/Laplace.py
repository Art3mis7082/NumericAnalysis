#Fecha de creación: 18 de mayo de 2026
#Tema: Ecuación de laplace para una placa rectangular
#Autor: Beatriz Almaraz

from numpy import  set_printoptions
from numpy import zeros, max

def llenarU(dimX,dimY):
    U=zeros((dimX,dimY))
    U[0,:]=100
    U[-1,:]=0
    U[:,0]=75
    U[:,-1]=50
    U[0,0]=(U[0,1]+U[1,0])/2
    U[0,-1]=(U[0,-2]+U[2,-1])/2
    U[-1,0]=(U[-2,0]+U[-1,1])/2

    U[-1,-1]=(U[-2,-1]+U[-1,-2])/2
    return U

def Laplace(U,tol,L):
    Ua=U*1.0
    Un=U*1.0
    R=Ua.shape[0]
    C=Ua.shape[1]
    errorU=zeros((R,C))
    i=0
    errorMaximo=tol+1
    while abs(errorMaximo)>=tol:
        for x in range(1,R-1):
            for y in range(1,C-1):
                Un[x,y]=(Ua[x+1,y]+Ua[x,y+1]+Ua[x-1,y]+Ua[x,y-1])/4
                Un[x,y]=L*Un[x,y]+(1-L)*Ua[x,y]
                errorU[x,y]=Un[x,y]-Ua[x,y];
                Ua[x,y]=Un[x,y];
                i=i+1
                errorMaximo=max(errorU);
    return Un,i


def graficaLaplace(U, elevacion=30, azimut=45):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    from numpy import arange, meshgrid

    R = U.shape[0]
    C = U.shape[1]
    x = arange(R)
    y = arange(C)
    X, Y = meshgrid(x, y)
    Z = U

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Configuración de la superficie
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False) # type: ignore
    
    # Etiquetas
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Ajuste de vista
    ax.view_init(elev=elevacion, azim=azimut)
    
    plt.show()

set_printoptions(suppress=True,precision=4,
                 linewidth=200,floatmode='fixed')
tol=0.01
L=1.5
Ua=llenarU(20,20)
print("Matriz U original:")
print(Ua)
[Un,i]=Laplace(Ua,tol,L)
print("La solución se encontró en i=",i)
print("Matriz U solución:")
print(Un)
graficaLaplace(Un, 30, 45)
