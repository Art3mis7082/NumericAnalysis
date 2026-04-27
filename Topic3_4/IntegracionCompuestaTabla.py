# Fecha de creacion: 22 de abril de 2026
# Tema: Integracion numerica compuesta con datos tabulados
# Autor: Beatriz Almaraz

import numpy as np


def trapecio_tabla(x, y):
    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud")
    if len(x) < 2:
        raise ValueError("Se requieren al menos 2 puntos")

    area_total = 0.0
    for i in range(len(x) - 1):
        h_i = x[i + 1] - x[i]
        area_total += h_i * (y[i] + y[i + 1]) / 2
    return area_total


def simpson_1_3_tabla(x, y):
    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud")

    n = len(x) - 1
    if n % 2 != 0:
        raise ValueError("Para Simpson 1/3 compuesto, n debe ser par")

    h = x[1] - x[0]
    if not np.allclose(np.diff(x), h):
        raise ValueError("Simpson 1/3 requiere puntos equiespaciados")

    suma_impares = np.sum(y[1:n:2])
    suma_pares = np.sum(y[2:n:2])
    area_total = h / 3 * (y[0] + y[n] + 4 * suma_impares + 2 * suma_pares)
    return area_total


def simpson_3_8_tabla(x, y):
    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud")

    n = len(x) - 1
    h = x[1] - x[0]
    if not np.allclose(np.diff(x), h):
        raise ValueError("Simpson 3/8 requiere puntos equiespaciados")

    if n < 3:
        raise ValueError("Se requieren al menos 3 subintervalos")

    # Si n no es multiplo de 3, se combina 3/8 con 1/3 para cubrir todo [a,b].
    if n % 3 == 0:
        suma_no_mult_3 = np.sum([y[i] for i in range(1, n) if i % 3 != 0])
        suma_mult_3 = np.sum([y[i] for i in range(3, n, 3)])
        return 3 * h / 8 * (y[0] + y[n] + 3 * suma_no_mult_3 + 2 * suma_mult_3)

    # Resto 2: 3/8 en [0, n-2] y 1/3 en los ultimos 2 subintervalos.
    if n % 3 == 2:
        m = n - 2
        suma_no_mult_3 = np.sum([y[i] for i in range(1, m) if i % 3 != 0])
        suma_mult_3 = np.sum([y[i] for i in range(3, m, 3)])
        i_38 = 3 * h / 8 * (y[0] + y[m] + 3 * suma_no_mult_3 + 2 * suma_mult_3)
        i_13 = h / 3 * (y[m] + 4 * y[m + 1] + y[m + 2])
        return i_38 + i_13

    # Resto 1: 3/8 en [0, n-4] y 1/3 en los ultimos 4 subintervalos.
    m = n - 4
    suma_no_mult_3 = np.sum([y[i] for i in range(1, m) if i % 3 != 0])
    suma_mult_3 = np.sum([y[i] for i in range(3, m, 3)])
    i_38 = 3 * h / 8 * (y[0] + y[m] + 3 * suma_no_mult_3 + 2 * suma_mult_3)
    i_13 = h / 3 * (y[m] + y[m + 4] + 4 * (y[m + 1] + y[m + 3]) + 2 * y[m + 2])
    return i_38 + i_13


# Tabla original del problema (no equiespaciada)
x_tabla = np.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.7, 0.8, 1.2, 1.3, 1.4, 1.6, 1.8, 2.0])
y_tabla = np.array([1.000, 0.555, 0.025, -1.238, -2.627, -3.305, -3.937, -5.697, -5.926, -6.090, -6.313, -6.565, -7.040])

# Malla uniforme para metodos de Simpson
x_uniforme = np.arange(0.0, 2.0 + 1e-12, 0.1)
y_uniforme = np.interp(x_uniforme, x_tabla, y_tabla)

# h utilizada en cada metodo
h_trapecio_tramos = np.diff(x_tabla)
h_simpson_13 = x_uniforme[1] - x_uniforme[0]
h_simpson_38 = x_uniforme[1] - x_uniforme[0]

# Calculo con los 3 metodos
i_trapecio = trapecio_tabla(x_tabla, y_tabla)
i_simpson_13 = simpson_1_3_tabla(x_uniforme, y_uniforme)
i_simpson_38 = simpson_3_8_tabla(x_uniforme, y_uniforme)

print("Resultados de la integral en [0, 2]:")
print(f"h Trapecio por tramos: {h_trapecio_tramos}")
print(f"h Simpson 1/3: {h_simpson_13:0.3f}")
print(f"h Simpson 3/8: {h_simpson_38:0.3f}")
print(f"Trapecio compuesto (tabla original): {i_trapecio:0.6f}")
print(f"Simpson 1/3 compuesto (interpolacion lineal): {i_simpson_13:0.6f}")
print(f"Simpson 3/8 compuesto (interpolacion lineal): {i_simpson_38:0.6f}")
