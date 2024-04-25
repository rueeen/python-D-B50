'''
a.	Crear un script en Python que solicite una palabra, cuente cuantos caracteres “a” hay en la palabra. 
'''

palabra = input('Ingrese la palabra a contar\n').lower()
#hola
contar_a = 0

for c in palabra:
    # c = "h"
    # c = "o"
    # c = "l"
    # c = "a"
    if c == "a" or c == 'A':
        contar_a += 1
        
print(f"La cantidad de caracteres 'a' dentro de {palabra} es :{contar_a}")
