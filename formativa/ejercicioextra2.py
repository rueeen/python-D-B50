user = 'perico'
password = '1234Aa'


u = input('Ingrese su usuario\n').lower() # capitalize() upper() Dejar todo en Minusculas
p = input('Ingrese su contraseña\n')
contador = 0
while u != user and p != password:
    print('Ususario y contraseña invalidos. Ingrese nuevamente')
    u = input('Ingrese su usuario\n').lower() # capitalize() upper() Dejar todo en Minusculas
    p = input('Ingrese su contraseña\n')
    contador += 1

print('Ususario y contraseña validos')