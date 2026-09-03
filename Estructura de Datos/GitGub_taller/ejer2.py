"""Leer tres notas de un estudiante y mostrar su promedio.
Entrada: tres notas 
Proceso: Sumar las notas y dividir al numero de notas
Salida: Promedio"""

"""Bosquejo
n1 = 7
n2 = 8
n3 = 9
suma = 7 + 8 + 9 
promedio = suma / 3
presentar Promedio"""

n1 = float(input("Ingrese nota 1: "))
n2 = float(input("Ingrese nota 2: "))
n3 = float(input("Ingrese nota 3: "))

promedio = (n1 + n2 + n3) / 3

if promedio >= 7 :
    print(f"Su promedio es de: {promedio:.2f} esta Aprobado")
else :
    print(f"Su promedio es de: {promedio:.2f} esta Reprobado")
