'''
Decir si un numero es PRIMO o no lo es
'''

def validarPrimo(numero): # 9
#             i -> 2, 3, 4, 5, 6, 7, 8
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese un numero\n"))

resultado = validarPrimo(n)

if resultado == True:
    print('El numero es PRIMO')
else:
    print('NO es PRIMO')
    
    
# FUNCION LEN

palabra = 'Hola mundo'

print(len(palabra))

# for i in range(n):
# i toma los valores segun range
# range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(3, 10) -> 3, 4, 5, 6, 7, 8, 9
# range(3, 10, 2) -> 3, 5, 7, 9

# for i in 'Hola mundo':
# i -> H, o, l, a,  , m, u, n, d, o