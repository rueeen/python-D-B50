
def sumarNumeros(a, b):
    print(a+b)
    
#sumarNumeros(5) # Error, falta b

#Parametros por defecto
def multiplicarNumeros(a=2, b=3):
    print(a*b)

multiplicarNumeros(5) #15
multiplicarNumeros(b=5) #10
multiplicarNumeros() #6
multiplicarNumeros(3, 3) #9
multiplicarNumeros(b=4, a=1) #4
#multiplicarNumeros(4, a=1) # Error
#multiplicarNumeros(b=2, 1) # Error