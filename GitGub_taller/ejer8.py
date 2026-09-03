"""Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.
entrada: ingresar monto total
proceso: calcular el monto con el iva y aplicar descuento
salida: monto final + iva + descuento
"""
"""Bosquejo
total = 200
iva = total * 0.15
total_iva = total + iva
presentar 
"""

total = float(input("Ingrese el total a pagar: "))
descuento = total * 0.1
total_descuento = total - descuento
iva = total_descuento * 0.15
total_iva = total_descuento + iva

print(f"Descuento: {descuento:.2f}")
print(f"IVA: {iva}")
print(f"Su total a pagar a pagar con iva es: {total_iva:.2f}")