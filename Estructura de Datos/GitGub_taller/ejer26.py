"""Lee N números y muestra la suma de los pares y la suma de los impares por separado.
Entrada: cantidad de números N, valores numéricos individuales
proceso: recorrer N veces leyendo cada número, verificar si es divisible entre 2 para acumularlo en pares, o de lo contrario en impares
salida: suma total de números pares y suma total de números impares """

"""bosquejo
n : 4
numeros : 4, 7, 2, 5
suma_pares = 0, suma_impares = 0
num = 4 -> 4 % 2 == 0 -> suma_pares = 0 + 4 = 4
num = 7 -> 7 % 2 != 0 -> suma_impares = 0 + 7 = 7
num = 2 -> 2 % 2 == 0 -> suma_pares = 4 + 2 = 6
num = 5 -> 5 % 2 != 0 -> suma_impares = 7 + 5 = 12
presentar suma_pares y suma_impares """

n = int(input("Ingrese la cantidad de números a procesar: "))

suma_pares = 0
suma_impares = 0

for i in range(1, n + 1):
    num = int(input(f"Ingrese el número {i}: "))
    
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num

print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")