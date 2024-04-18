'''
Conversor de monedas (Dólar a CLP) solicitando el valor actual 
del dólar y la cantidad de dólares al usuario
'''

valor_dolar = 980
cantidad_dolar = float(input('Ingrese cantidad en dolares\n'))

clp = valor_dolar * cantidad_dolar

print(f'Los {cantidad_dolar} dolare a peso son: {clp}')

