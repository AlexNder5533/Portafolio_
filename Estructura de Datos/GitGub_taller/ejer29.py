"""Muestra los primeros N números de Fibonacci.
La serie: 0, 1, 1, 2, 3, 5, 8, 13, 21... Cada número es la suma de los dos anteriores.
Entrada: cantidad de términos N (entero positivo)
proceso: inicializar los dos primeros valores (a=0, b=1) y en cada paso generar el siguiente sumándolos y actualizando variables
salida: secuencia con los primeros N términos de Fibonacci """

"""bosquejo
n : 5
a = 0, b = 1
i = 1 -> mostrar 0 -> a = 1, b = 1
i = 2 -> mostrar 1 -> a = 1, b = 2
i = 3 -> mostrar 1 -> a = 2, b = 3
i = 4 -> mostrar 2 -> a = 3, b = 5
i = 5 -> mostrar 3 -> fin """

n = int(input("Ingrese la cantidad de números de Fibonacci a mostrar: "))

if n <= 0:
    print("Por favor, ingrese un número mayor a 0.")
else:
    a, b = 0, 1
    print("Serie de Fibonacci:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()