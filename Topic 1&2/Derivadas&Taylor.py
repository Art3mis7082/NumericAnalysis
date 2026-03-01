#Fecha de creación: 13 de febrero de 2026
#Tema: Derivadas sucesivas y polinomio de Taylor
#Autor: Beatriz Almaraz

from sympy import Symbol,cos,sin, diff, lambdify, exp, log, symbols

a, x, X = symbols('a x X')
f=log(x); print(f"f = {f}")

f1=diff(f,x, 1); print(f"f1 = {f1}")
f2=diff(f,x, 2); print(f"f2 = {f2}")
f3=diff(f,x, 3); print(f"f3 = {f3}")
f4=diff(f,x, 4); print(f"f4 = {f4}")
f5=diff(f,x, 5); print(f"f5 = {f5}")

p=f+f1*(X-a)**1/1+f2*(X-a)**2/2+f3*(X-a)**3/6+f4*(X-a)**4/24+f5*(X-a)**5/120; 

Px=p.subs([(x,1), (a,1)])
print(f"Px = {Px}")

Pnumerico = lambdify(X, Px)
print(f"P(0.125) = {Pnumerico(0.125)}")