"""Leer las notas de N estudiantes, contar aprobados (nota >= 70), reprobados y calcular el porcentaje de aprobación.
Entrada: cantidad de estudiantes N, notas individuales
proceso: recorrer N veces leyendo cada nota, verificar si es >= 70 para sumar a aprobados o si no a reprobados, y calcular el porcentaje
salida: cantidad de aprobados, cantidad de reprobados y porcentaje de aprobación """

"""bosquejo
n : 4
notas : 80, 65, 90, 70
i = 1 -> nota = 80 (aprobados = 1)
i = 2 -> nota = 65 (reprobados = 1)
i = 3 -> nota = 90 (aprobados = 2)
i = 4 -> nota = 70 (aprobados = 3)
porcentaje_aprobados = (3 / 4) * 100 = 75.0%
presentar resultados """

n = int(input("Ingrese la cantidad de estudiantes: "))

if n <= 0:
    print("La cantidad de estudiantes debe ser mayor a 0.")
else:
    aprobados = 0
    reprobados = 0

    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        if nota >= 70:
            aprobados += 1
        else:
            reprobados += 1

    porcentaje_aprobados = (aprobados / n) * 100

    print(f"Estudiantes aprobados: {aprobados}")
    print(f"Estudiantes reprobados: {reprobados}")
    print(f"Porcentaje de aprobación: {porcentaje_aprobados:.2f}%")