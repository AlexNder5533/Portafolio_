"""Leer las notas de N estudiantes y mostrar la nota más alta y la más baja.
Entrada: cantidad de estudiantes N, notas individuales
proceso: inicializar maxima en float("-inf") y minima en float("inf"), recorrer N veces actualizando ambos valores con cada nota ingresada
salida: la nota más alta y la nota más baja """

"""bosquejo
n : 4
notas : 85, 60, 92, 75
maxima = -inf, minima = inf
i = 1 -> nota = 85 (maxima = 85, minima = 85)
i = 2 -> nota = 60 (maxima = 85, minima = 60)
i = 3 -> nota = 92 (maxima = 92, minima = 60)
i = 4 -> nota = 75 (maxima = 92, minima = 60)
presentar maxima y minima """

n = int(input("Ingrese la cantidad de estudiantes: "))

if n <= 0:
    print("La cantidad de estudiantes debe ser mayor a 0.")
else:
    maxima = float("-inf")
    minima = float("inf")

    for i in range(1, n + 1):
        nota = float(input(f"Ingrese la nota del estudiante {i}: "))
        
        if nota > maxima:
            maxima = nota
        if nota < minima:
            minima = nota

    print(f"La nota más alta es: {maxima}")
    print(f"La nota más baja es: {minima}")