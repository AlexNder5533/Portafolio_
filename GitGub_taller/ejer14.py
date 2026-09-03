"""Lee peso (kg) y estatura (m) y calcula el IMC. Fórmula: IMC = peso / estatura². Muestra el IMC con 2 decimales.
Entrada: peso (kg), estatura (m)
proceso: calcular el IMC dividiendo el peso entre la estatura al cuadrado
salida: IMC con 2 decimales """

"""bosquejo
peso : 70.5
estatura : 1.75
imc = peso / (estatura ** 2)
presentar imc """

peso = float(input("Ingrese el peso en kg: "))
estatura = float(input("Ingrese la estatura en metros: "))

imc = peso / (estatura ** 2)

print(f"Su IMC es: {imc:.2f}")