"""Leer un número y determinar si es primo, y generar la lista de primos del 2 al 100.
Entrada: un número entero N
proceso: 
  1. Comprobar si N es primo verificando si no tiene divisores desde 2 hasta su raíz cuadrada.
  2. Recorrer los números del 2 al 100 y agregar a una lista aquellos que sean primos.
salida: mensaje indicando si N es primo o no, y la lista de primos del 2 al 100 """

"""bosquejo
numero : 7
7 <= 1 -> no
probar divisores desde 2 hasta 6 -> ninguno divide exacto -> 7 es primo
rango 2 a 100 -> evaluar cada uno y acumular en lista
presentar resultado del número y lista de primos """

# Parte 1: Determinar si un número ingresado es primo
num = int(input("Ingrese un número entero: "))

if num <= 1:
    es_primo = False
else:
    es_primo = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            es_primo = False
            break

if es_primo:
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")

primos = []

for n in range(2, 101):
    primo_actual = True
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            primo_actual = False
            break
    if primo_actual:
        primos.append(n)

print(f"Números primos entre 2 y 100: {primos}")