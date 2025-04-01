def descuento_productos():
    cantidad = int(input("Ingrese la cantidad de productos: "))
    precio_unitario = float(input("Ingrese el precio unitario: "))
    total = cantidad * precio_unitario
    descuento = total * 0.10
    precio_final = total - descuento
    print("El total con un 10% de descuento es:", precio_final)