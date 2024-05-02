'''
c.	Cree una función en python que reciba un número, escriba si el número es par o impar.
'''

def parImpar(n):
    if n % 2 == 0:
        print('Es par')
    else:
        print('Es impar')
        
numero = int(input('Ingrese un numero\n'))

parImpar(numero)