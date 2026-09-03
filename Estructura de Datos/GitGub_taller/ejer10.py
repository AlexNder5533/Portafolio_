"""Leer una cantidad total de segundos y mostrarla como hh:mm:ss. Ejemplo: 3725 segundos → 01:02:05.
entrada: segundos totales, horas,mm,ss
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

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

tiempo_total = input("Ingrese la hora: (hh:mm:ss) ")
horas, minutos, segundos = tiempo_total.split(":")
total_segundos = (int(horas) * 3600) + (int(minutos) * 60) + int(segundos)

print(f"La hora en segundos es de: {total_segundos}")

