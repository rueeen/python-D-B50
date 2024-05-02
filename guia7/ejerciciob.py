'''
b.	Cree una función en python que reciba una palabra, cuente cuantas vocales 
(a, e, i, o, u) hay dentro de la palabra.
'''

def contarVocales(palabra):
    #palabra = 'hola'
    contador = 0
    for c in palabra:
        if "a" == c or "e" == c or "i" == c or "o" == c or "u" == c:
            contador += 1
    
    print(f'La cantidad de vocales es {contador}')
    
p = input('Ingrese una palabra\n')

contarVocales(p)


