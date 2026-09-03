"""Un producto vale $12. Si compras 10 o más te dan 15% de descuento, si compras entre 5 y 9 te dan 5%. Calcula el total.
Entrada: cantidad de productos
proceso: calcular subtotal, aplicar el porcentaje de descuento según el rango de unidades y restar el descuento
salida: total a pagar """

"""bosquejo
precio_unitario : 12
cantidad : 10
subtotal = 10 * 12 = 120
si cantidad >= 10 -> descuento = 0.15 * 120 = 18
total = 120 - 18 = 102
presentar total """

PRECIO_UNITARIO = 12.0
cantidad = int(input("Ingrese la cantidad de productos: "))

subtotal = cantidad * PRECIO_UNITARIO

if cantidad >= 10:
    descuento = subtotal * 0.15
elif cantidad >= 5:
    descuento = subtotal * 0.05
else:
    descuento = 0.0

total = subtotal - descuento

print(f"Total a pagar: ${total:.2f}")