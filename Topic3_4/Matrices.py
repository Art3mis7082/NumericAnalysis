#Fecha de creación: 2 de marzo de 2026
#Tema: Inversa de una matriz
#Nombre: Almaraz García Beatriz

from numpy import matrix
from numpy.linalg import inv, det

A=matrix([[1,2],[7,4]])

print(A)
print(det(A))
print(inv(A))
print(A**(-1))