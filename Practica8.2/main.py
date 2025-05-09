import numpy as np

def romberg_integration(func, a, b, max_n=10, tol=None):
    R = [[0.0 for _ in range(max_n)] for _ in range(max_n)]
    h = b - a
    R[0][0] = 0.5 * h * (func(a) + func(b))

    for i in range(1, max_n):
        h /= 2.0
        sum_f = sum(func(a + (k - 0.5) * h * 2) for k in range(1, 2 ** i + 1))
        R[i][0] = 0.5 * R[i - 1][0] + h * sum_f

        for j in range(1, i + 1):
            R[i][j] = (4 ** j * R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)

        if tol is not None and abs(R[i][i] - R[i - 1][i - 1]) < tol:
            return R, i + 1

    return R, max_n

def imprimir_tabla(R, niveles):
    print("\nTabla de Romberg (R[i][j]):")
    for i in range(niveles):
        fila = [f"{R[i][j]:.6f}" if j <= i else "" for j in range(niveles)]
        print(f"Nivel {i+1}: " + "\t".join(fila))

def opcion_1():
    print("\n=== Opción 1: Evaluar función ingresada por el usuario ===")
    func_str = input("Ingresa la función f(x): ")
    a = float(input("Límite inferior a: "))
    b = float(input("Límite superior b: "))
    n = int(input("Número de niveles de Romberg (n > 0): "))

    def func(x):
        return eval(func_str, {"np": np, "x": x})

    try:
        R, _ = romberg_integration(func, a, b, max_n=n)
        print(f"\n✅ Resultado: R[{n},{n}] = {R[n - 1][n - 1]:.6f}")
    except Exception as e:
        print("\n⛔ Error al evaluar la función. Verifica la sintaxis.")
        print(str(e))

def opcion_2():
    print("\n=== Opción 2: Funciones aproximadas===")

    def f_a(x):
        return x ** (1 / 3)

    def f_b(x):
        if 0 <= x <= 0.1:
            return x ** 3 + 1
        elif 0.1 < x <= 0.2:
            return 1.001 + 0.03*(x - 0.1) + 0.3*(x - 0.1)**2 + 2*(x - 0.1)**3
        elif 0.2 < x <= 0.3:
            return 1.009 + 0.15*(x - 0.2) + 0.9*(x - 0.2)**2 + 2*(x - 0.2)**3
        else:
            return 0

    R_a, niveles_a = romberg_integration(f_a, 0, 1)
    print(f"\na) ∫₀¹ x^(1/3) dx ≈ {R_a[niveles_a - 1][niveles_a - 1]:.6f}")
    imprimir_tabla(R_a, niveles_a)

    R_b, niveles_b = romberg_integration(f_b, 0, 0.3)
    print(f"\nb) ∫₀^{0.3} f(x) dx ≈ {R_b[niveles_b - 1][niveles_b - 1]:.6f}")
    imprimir_tabla(R_b, niveles_b)

def opcion_3():
    print("\n=== Opción 3: Evaluar funcion")

    def f(x):
        return np.sqrt(1 + (np.cos(x))**2)

    R, _ = romberg_integration(f, 0, 48, max_n=11)

    print("\n--- a) R[i,1] para i = 1 a 5 ---")
    for i in range(5):
        print(f"R[{i+1},1] = {R[i][0]:.8f}")

    print("\n--- b) R[i,i] para i = 2 a 5 ---")
    for i in range(1, 5):
        print(f"R[{i+1},{i+1}] = {R[i+1][i+1]:.8f}")

    print("\n--- c) R[i,i] para i = 6 a 10 ---")
    for i in range(5, 10):
        print(f"R[{i+1},{i+1}] = {R[i+1][i+1]:.8f}")

    print("\n--- d) Resultado estimado ---")
    print(f"R[10,10] = {R[10][10]:.8f}")

    print("\n--- e) Comentario ---")
    print("La integral oscila mucho por el cos(x), lo que requiere muchos subintervalos.")
    print("Una mejora posible sería aplicar un cambio de variable que suavice la oscilación.")

def main():
    while True:
        print("\n=== Menú de Integración de Romberg ===")
        print("1. Ingresar una función manualmente")
        print("2. Evaluar funciones predefinidas (incisos a y b)")
        print("3. Evaluar ∫₀⁴⁸ √(1 + (cos x)²) dx (caso especial)")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()



