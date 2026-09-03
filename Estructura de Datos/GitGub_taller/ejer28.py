"""Genera un número secreto entre 1 y 100. El usuario intenta adivinar.
En cada intento le dices si es «mayor» o «menor». Cuenta cuántos intentos usó.
Entrada: intentos sucesivos del usuario (números enteros)
proceso: 
  1. Generar número aleatorio entre 1 y 100.
  2. Repetir mientras no adivine: leer intento, incrementar contador y dar pista (mayor/menor).
salida: mensaje de acierto con la cantidad total de intentos empleados """

"""bosquejo
secreto : 42
intento 1: 50 -> "El número secreto es menor"
intento 2: 25 -> "El número secreto es mayor"
intento 3: 42 -> "Adivinaste en 3 intentos" """

import random

secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("¡He generado un número entre 1 y 100! Intenta adivinarlo.")

while not adivinado:
    intento = int(input("Ingresa tu número: "))
    intentos += 1

    if intento < secreto:
        print("El número secreto es mayor.")
    elif intento > secreto:
        print("El número secreto es menor.")
    else:
        adivinado = True
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")