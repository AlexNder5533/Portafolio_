"""Lee un número de 3 cifras y muestra la suma de sus dígitos. Ejemplo: 435 → 4+3+5 = 12.
Entrada: numero de tres centenas
proceso: Separar el numero y simar sus valores
salida: suma de los numeros"""

"""Bosquejo
num = 456
4 + 5 + 6
presentar suma """

num = int(input("Ingrese un numero en centena: "))
resto = num
centenas = num // 100
decenas = (num // 10) % 10
unidad = num % 10

suma = centenas + decenas + unidad
print(f"La suma de los valores es: {suma}")