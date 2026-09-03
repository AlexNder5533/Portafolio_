"""Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.
entrada: ingresar monto total
proceso: calcular el monto con el iva 
salida: monto final + iva
"""
"""Bosquejo
total = 200
iva = total * 0.15
total_iva = total + iva
presentar 
"""

total = float(input("Ingrese el total a pagar: "))
iva = total * 0.15
total_iva = total + iva
print(f"IVA: {iva}")
print(f"Su total a pagar a pagar con iva es: {total_iva:.2f}")
