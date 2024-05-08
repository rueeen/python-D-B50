def contarCaracteres(palabra):
    contador = 0
    for caracter in palabra:
        if caracter != ' ':
            contador += 1
    return contador