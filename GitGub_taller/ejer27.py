"""Pide una edad y valida que esté entre 0 y 120. Si el usuario ingresa algo inválido, vuelve a pedirla.
Entrada: edad (número entero)
proceso: solicitar la edad en un bucle repetitivo hasta que el valor sea mayor o igual a 0 y menor o igual a 120
salida: edad válida confirmada """

"""bosquejo
edad : -5  -> inválido, volver a pedir
edad : 130 -> inválido, volver a pedir
edad : 20  -> válido, salir del bucle
presentar edad ingresada """

while True:
    edad = int(input("Ingrese su edad (0 - 120): "))
    if 0 <= edad <= 120:
        break
    print("Edad inválida. Debe estar entre 0 y 120.")

print(f"Edad válida registrada: {edad}")
