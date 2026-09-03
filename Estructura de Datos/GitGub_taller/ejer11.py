"""Un cajero solo tiene billetes de $20, $10, $5 y $1. Dado un monto, mostrar cuántos billetes de cada uno se necesitan (usando la mínima cantidad).
entrada: ingresa el monto a retirar
proceso: mostrar cuantos billetes de cada tipo se necesitan
salida: catidad de billetes para la cantidad """
"""Bosquejo
monto = 87
$20: 87 // 20 = 4, sobra 7
$10:  7 // 10 = 0, sobra 7
$5 :  7 //  5 = 1, sobra 2
$1 :  2 //  1 = 2, sobra 0 """

monto = float(input("Ingrese el monto: "))
resto = round(monto * 100)
b50 = resto // 5000; resto = resto % 5000
b20 = resto // 2000; resto = resto % 2000
b10 = resto // 1000; resto = resto % 1000
b05 = resto // 500; resto = resto % 500
b01 = resto // 100; resto = resto % 100

m50 = resto // 50; resto = resto % 50
m25 = resto // 25; resto = resto % 25
m05 = resto // 5; resto = resto % 5
m01 = resto

print(f"$50 x {b50}")
print(f"$20 x {b20}")
print(f"$10 x {b10}")
print(f"$5 x {b05}")
print(f"$1 x {b01}")
print(f"Monedas de 50¢:   {m50}")
print(f"Monedas de 25¢:   {m25}")
print(f"Monedas de 5¢:    {m05}")
print(f"Monedas de 1¢:    {m01}")