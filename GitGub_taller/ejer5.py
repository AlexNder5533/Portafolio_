"""Pide un total de segundos y muéstralos como hh:mm:ss. Ej.: 3725 segundos → 1:02:05.
entrada: segundos totales
proceso: cambiarlos a horas minutos y segundos como un cronometro
salida: mostrar las horas, minutos y segundos"""

"""Bosquejo
segundos = 5200
horas = segundos // 3600
resto = segundos % 3600
minutos resto // 60
segundos resto % 60
presentar """

segundos = int(input("Ingrese los segundos totales: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos:02d}:{segundos:02d}")