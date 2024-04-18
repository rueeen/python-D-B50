valor_producto = int(input("Ingrese valor producto\n"))
descuento_producto = int(input("Ingrese descuento producto\n"))

valor_final = valor_producto - (valor_producto*descuento_producto/100)

print(f"El valor final del producto es {valor_final}")