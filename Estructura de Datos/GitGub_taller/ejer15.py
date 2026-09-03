"""Lee un número decimal y una cantidad de decimales, y muéstralo redondeado. Ejemplo: 3.14159 con 2 decimales → 3.14.
Entrada: numero decimal, cantidad de decimales
proceso: redondear el numero a la cantidad de decimales indicada
salida: numero redondeado """

"""bosquejo
numero : 3.14159
decimales : 2
redondeado = round(numero, decimales)
presentar redondeado """

numero = float(input("Ingrese el número decimal: "))
decimales = int(input("Ingrese la cantidad de decimales: "))

redondeado = round(numero, decimales)

print(f"{redondeado}")