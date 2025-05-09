import numpy as np

def romberg_integration(func, a, b, tol=1e-4, max_n=10):
    R = [[0.0 for _ in range(max_n)] for _ in range(max_n)]
    h = b - a
    R[0][0] = 0.5 * h * (func(a) + func(b))

    for i in range(1, max_n):
        h /= 2.0
        sum_f = sum(func(a + (k - 0.5) * h * 2) for k in range(1, 2 ** i + 1))
        R[i][0] = 0.5 * R[i - 1][0] + h * sum_f

        for j in range(1, i + 1):
            R[i][j] = (4 ** j * R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)

        if abs(R[i][i] - R[i - 1][i - 1]) < tol:
            return R, i + 1  # Devolver toda la tabla y niveles usados

    return R, max_n

# Función para imprimir la tabla R
def imprimir_tabla(R, niveles):
    print("\nTabla de Romberg (R[i][j]):")
    for i in range(niveles):
        fila = [f"{R[i][j]:.6f}" if j <= i else "" for j in range(niveles)]
        print(f"Nivel {i+1}: " + "\t".join(fila))

# Función del inciso a)
def f_a(x):
    return x ** (1 / 3)

# Función por tramos del inciso b)
def f_b(x):
    if 0 <= x <= 0.1:
        return x ** 3 + 1
    elif 0.1 < x <= 0.2:
        return 1.001 + 0.03*(x - 0.1) + 0.3*(x - 0.1)**2 + 2*(x - 0.1)**3
    elif 0.2 < x <= 0.3:
        return 1.009 + 0.15*(x - 0.2) + 0.9*(x - 0.2)**2 + 2*(x - 0.2)**3
    else:
        return 0

# Ejecución para ambos incisos
print("=== Integración de Romberg ===")

# Inciso a
R_a, niveles_a = romberg_integration(f_a, 0, 1)
print(f"\na) ∫₀¹ x^(1/3) dx ≈ {R_a[niveles_a - 1][niveles_a - 1]:.6f}")
print(f"Niveles usados: {niveles_a}")
imprimir_tabla(R_a, niveles_a)

# Inciso b
R_b, niveles_b = romberg_integration(f_b, 0, 0.3)
print(f"\nb) ∫₀^{0.3} f(x) dx ≈ {R_b[niveles_b - 1][niveles_b - 1]:.6f}")
print(f"Niveles usados: {niveles_b}")
imprimir_tabla(R_b, niveles_b)

