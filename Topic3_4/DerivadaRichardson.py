#Fecha de creación: 17 de abril de 2026
#Tema: Derivada Richardson
#Autor: Almaraz Garcia Beatriz

from numpy import cos, sin


def D3r(f, X0, h):
    # Tercera derivada regresiva con error de orden O(h)
    D = (f(X0) - 3 * f(X0 - h) + 3 * f(X0 - 2 * h) - f(X0 - 3 * h)) / h**3
    return D


f = lambda x: cos(3 * x**2)
X0 = 2
h = 0.001

# f'''(x) para f(x)=cos(3x^2): 216*x^3*sin(3x^2) - 108*x*cos(3x^2)
Vr = 216 * X0**3 * sin(3 * X0**2) - 108 * X0 * cos(3 * X0**2)
print(f"Valor real de la 3 derivada = {Vr:0.6f}")

D3h = D3r(f, X0, h)
print(f"3 derivada regresiva con h = {D3h:0.6f}")

D3h_1_2 = D3r(f, X0, h / 2)
print(f"3 derivada regresiva con h/2 = {D3h_1_2:0.6f}")

# D3r tiene error O(h), por eso en Richardson se usa p=1.
Richardson = 2 * D3h_1_2 - D3h
print(f"3 derivada por Richardson = {Richardson:0.6f}")

ERPh = abs((Vr - D3h) / Vr) * 100
ERPh2 = abs((Vr - D3h_1_2) / Vr) * 100
ERPR = abs((Vr - Richardson) / Vr) * 100

print(f"ERPh (h) = {ERPh:0.6f}%")
print(f"ERPh2 (h/2) = {ERPh2:0.6f}%")
print(f"ERPR (Richardson) = {ERPR:0.6f}%")