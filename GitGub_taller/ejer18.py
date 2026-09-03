"""Leer N y calcular la suma de 1 + 2 + 3 + ... + N.
Entrada: numero N
proceso: acumular la suma de todos los enteros desde 1 hasta N
salida: suma total """

"""bosquejo
n : 4
suma = 0
i = 1 -> suma = 0 + 1 = 1
i = 2 -> suma = 1 + 2 = 3
i = 3 -> suma = 3 + 3 = 6
i = 4 -> suma = 6 + 4 = 10
presentar suma """

n = int(input("Ingrese un número N: "))
suma_n = 0

for i in range(1, n + 1):
    suma_n += i

print(f"La suma del 1 al {n} es: {suma_n}")

suma_pares = 0

for i in range(2, 101, 2):
    suma_pares += i

print(f"La suma de los pares del 2 al {n} es: {suma_pares}")