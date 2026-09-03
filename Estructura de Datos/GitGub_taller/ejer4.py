"""Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: F = C × 9/5 + 32.
Entrada: temperatura en celsius
Proceso: combertirla a fahrenheit
Salida: temperatura en fahrenheit"""

"""Bosquejo
temp = 25
temp_fahrenheit = temp * 9 / 5 + 32
mostrar temperatura """

temp = float(input("Ingrese la temperatura en celsius: "))

temp_fahrenheit = temp * 9 / 5 + 32
print(f"La temperatura en Fahrenheit es: {temp_fahrenheit:.2f}")