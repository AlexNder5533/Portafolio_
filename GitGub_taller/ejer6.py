"""Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS.
entrada: dos numeros
proceso: cambiar el valor de las variables 
salida: mostar los valores cambiados """

"""bosquejo
n1 = 8
n2 = 9
n1 , n2 = n2 , n1
presentar los valores"""

n1 = int(input("ingrese numero 1: "))
n2 = int(input("ingrese numero 2: "))

n1, n2 = n2, n1
print (f"{n1} {n2}")