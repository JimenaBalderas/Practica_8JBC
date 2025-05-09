import numpy as np

def romberg_integration(func_str, a, b, n):
    # Define una función evaluable desde el string ingresado
    def func(x):
        return eval(func_str, {"np": np, "x": x})

    R = [[0.0 for _ in range(n)] for _ in range(n)]

    h = b - a
    R[0][0] = 0.5 * h * (func(a) + func(b))

    for i in range(1, n):
        h /= 2.0
        sum_f = sum(func(a + (k - 0.5) * h * 2) for k in range(1, 2 ** i + 1))
        R[i][0] = 0.5 * R[i - 1][0] + h * sum_f

        for j in range(1, i + 1):
            R[i][j] = (4 ** j * R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)

    return R[n - 1][n - 1]

# -------- Ejecución principal en bucle ----------
if __name__ == "__main__":
    print("=== Integración de Romberg ===")

    while True:
        print("\n Usa funciones de numpy como: x**2, np.sin(x), np.log(x), etc.")
        func_str = input("Ingresa la función f(x): ")
        a = float(input("Ingresa el límite inferior a: "))
        b = float(input("Ingresa el límite superior b: "))
        n = int(input("Ingresa el número de niveles de Romberg (n > 0): "))

        try:
            resultado = romberg_integration(func_str, a, b, n)
            print(f"\n Resultado de la integral usando Romberg R[{n},{n}] = {resultado:.6f}")
        except Exception as e:
            print("\n Error al evaluar la función. Verifica que usaste sintaxis correcta.")
            print("   Ejemplo válido: x**2 * np.log(x)")

        # Preguntar si desea continuar
        repetir = input("\n¿Deseas calcular otra integral? (s/n): ").strip().lower()
        if repetir != 's':
            print(" Programa finalizado.")
            break



