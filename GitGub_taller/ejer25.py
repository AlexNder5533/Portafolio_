"""Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).
Entrada: un número entero
proceso: tomar el valor absoluto, dividir sucesivamente entre 10 con división entera // hasta llegar a 0 e incrementar un contador
salida: cantidad total de dígitos """

"""bosquejo
numero : 456
temp = 456
contador = 0
456 // 10 = 45 -> contador = 1
45 // 10 = 4   -> contador = 2
4 // 10 = 0    -> contador = 3
presentar contador """

num = int(input("Ingrese un número entero: "))

temp = abs(num)
contador = 0

if temp == 0:
    contador = 1
else:
    while temp > 0:
        contador += 1
        temp //= 10

print(f"El número tiene {contador} dígitos.")