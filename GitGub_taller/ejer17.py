"""Leer un número N y mostrar los números del 1 al N.
Entrada: numero N
proceso: recorrer los numeros enteros desde 1 hasta N
salida: secuencia de numeros del 1 al N """

"""bosquejo
n : 5
para i desde 1 hasta 5:
presentar i """

n = int(input("INGRESE LAS VECES QUE SE REPITE: "))
for i in range(n, 0, -1) :
    print(i)

