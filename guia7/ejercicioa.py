'''
a.	Cree una función en python que reciba 2 números, imprima un mensaje con el mayor de ellos.
'''

def mostrarMayorOigual(n, m):
    if n > m:
        print(f'El mayor es {n}')
    elif n < m:
        print(f'El mayor es {m}')
    else:
        print('Son iguales')
        
n = float(input('Ingrese un numero\n'))
m = float(input('Ingrese otro numero\n'))

mostrarMayorOigual(m, n)
    