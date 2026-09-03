"""Leer N y calcular el factorial (N! = 1 * 2 * 3 * ... * N).
Entrada: numero entero N
proceso: inicializar acumulador en 1 y multiplicar sucesivamente desde 1 hasta N
salida: resultado del factorial N! """

"""bosquejo
n : 5
factorial = 1
i = 1 -> factorial = 1 * 1 = 1
i = 2 -> factorial = 1 * 2 = 2
i = 3 -> factorial = 2 * 3 = 6
i = 4 -> factorial = 6 * 4 = 24
i = 5 -> factorial = 24 * 5 = 120
presentar factorial """

n = int(input("Ingrese un número entero no negativo N: "))

if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(f"{n}! = {factorial}")