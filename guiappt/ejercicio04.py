pies = float(input("Ingrese pies a convertir\n"))

metros = pies * 0.3048
#round es una funcion para redondear
# round(cantidad_a_redondear, numero_de_decimales)
print(f"Los {pies} pies a metros son {round(metros, 3)}")