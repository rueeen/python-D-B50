'''
Solo entre numeros
y solo entre str
'a' > 1 -> ERROR
3 < 2 -> False
5 >= 3 -> True
'a' <= 'b' ->
'''
def contarCaracteres(palabra):
    contador = 0
    for caracter in palabra:
        if caracter != ' ':
            contador += 1
    return contador
    print('No se ejecuta')

p1 = input('Ingrese una palabra\n')
p2 = input('Ingrese otra palabra\n')

r1 = contarCaracteres(p1)
r2 = contarCaracteres(p2)

if r1 > r2:
    print(f'{p1} es mas larga que {p2}')
else:
    print(f'{p2} es mas larga que {p1}')