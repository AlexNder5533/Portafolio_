"""Leer un número entero y determinar si es par o impar.
entrada:leer un numero 
proceso: verificar si es par o impar
salida: mensaje que si es par o impar """
""" Bosquejo 
num = 7 
if num % 2 == 0 :
    es par
else :
    es impar
"""

num = int(input("ingrese un numero: "))
if num % 2 == 0:
    print(f"El numero es Par")
else :
    print(f"El numero es Impar")

if num % 5 == 0 and num % 3 == 0:
    print(f"el numero es multiplo de ambos")
elif num % 5 == 0:
    print(f"El numero es multiplo de 5")
elif num % 3 == 0:
    print(f"El numero es multiplo de 3")
else :
    print(f"el numero no es multiplo de 3 o 5")

    