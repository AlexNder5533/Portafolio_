"""Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
Entrada: un número entero N
proceso: iterar desde 1 hasta 12 multiplicando N por el contador de cada ciclo
salida: tabla de multiplicar del 1 al 12 en formato N x i = resultado """

"""bosquejo
n : 5
para i desde 1 hasta 12:
    resultado = 5 * i
    presentar 5 x i = resultado """

n = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 13):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")