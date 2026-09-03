"""Lee una cantidad de minutos y muéstrala como «X horas Y minutos». Ejemplo: 135 → «2 horas 15 minutos».
Entrada: minutos totales
proceso: separar las horas y minutos
salida: horas y minutos """

"""bosquejo
minutos_totales : 152
horas = (nimutos // 60) % 60
minutos = minutos totales % 60
presentar hora """

minutos_totales = int(input("ingrese los minutos: "))
resto = minutos_totales

horas = (resto // 60) % 60
minutos = resto % 60
print(f"{horas:02d}:{minutos:02d}")