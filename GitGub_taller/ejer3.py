"""Leer la base y la altura de un rectángulo y mostrar su área y su perímetro. 
Recuerda: área = base × altura, perímetro = 2 × (base + altura).
Entrada: Base y altura del rectangulo
Proceso: hallar el area y el perimetro
Salida: mostrar el area y perimetro"""

"""Bosquejo
Base: 15
Altura: 7
area= base * altura
perimetro = area * 2
Presentar el area y perimetro"""
base = float(input("Ingrese la medida de la base: "))
altura = float(input("Ingrese la altura: "))
radio = float(input("Ingrese el radio del circulo: "))

area = base * altura
Perimetro = 2 * (base + altura)
import math
area_circulo = math.pi * radio**2
perimetro_circulo = 2 * math.pi * radio

print(f"El area del rectangulo es de: {area:.2f}")
print(f"El perimetro del rectangulo es de: {Perimetro:.2f}")
print(f"El area del Circulo es de: {area_circulo:.2f}")
print(f"El perimetro del Circulo es de: {perimetro_circulo:.2f}")

