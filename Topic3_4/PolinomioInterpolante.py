#Fecha de creación: 13 de abril de 2026
#Tema: Polinomio newton progresivo y regresivo
#Autor: Beatriz Almaraz Garcia

from math import factorial

def PolyInterpolante(X, X0, Y0, h, Vd, Tp):
    n = len(Vd)
    if (Tp==1):
        s=(X-X0)/h #Progresivo
    elif (Tp==2):
        s=(X-X0)/h #Regresivo
    else:
        raise ValueError("Tp debe ser 1 (progresivo) o 2 (regresivo)")

    S = s
    Y = Y0

    for i in range(n):
        VS = Vd[i]*S/factorial(i+1)
        Y = Y + VS
        if (Tp==1):
            S = S*(s-(i+1))
        if (Tp==2):
            S = S*(s+(i+1))
        #print("Vd[",i,"] = ", Vd[i], " S = ", S, " VS = ", VS, " Y = ", Y)

    return Y

def DiferenciasProgresivas(y_datos):
    tabla = [y_datos[:]]
    while len(tabla[-1]) > 1:
        anterior = tabla[-1]
        actual = [anterior[i + 1] - anterior[i] for i in range(len(anterior) - 1)]
        tabla.append(actual)
    return tabla


# Datos de la tabla del ejercicio
X_datos = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
Y_datos = [0.000, 0.041, 0.079, 0.114, 0.146, 0.176, 0.204, 0.230, 0.255, 0.279, 0.301]

h = X_datos[1] - X_datos[0]  # 0.1
Tp = 2  # Regresivo
X0 = X_datos[0]
Y0 = Y_datos[0]

# Vd = [ΔY0, Δ2Y0, Δ3Y0, ... , Δ10Y0]
tabla_dif = DiferenciasProgresivas(Y_datos)
Vd = [tabla_dif[orden][0] for orden in range(1, len(tabla_dif))]

#X_evaluar = [1.05, 1.14, 1.37] #Puntos para forma progresiva
X_evaluar = [1.74, 1.83, 1.92] #Puntos para forma regresiva

print("Polinomio de Newton-Gregory regresivo usando todos los datos:")

for X in X_evaluar:
    Y = PolyInterpolante(X, X0, Y0, h, Vd, Tp)
    print(f"Para X = {X:.2f}, Y aprox = {Y:.10f}")
