n = float(input('Ingrese un numero\n'))
m = float(input('Ingrese otro numero\n'))

if n > m :
    print(f'{n} es mayor que {m}')
elif n < m:
    print(f'{m} es mayor que {n}')
else:
    print('Son iguales')