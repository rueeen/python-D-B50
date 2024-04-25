#Orden de ejecucion de funcion


def funcion_resta(a, b):
    print(a - b)
    
n = int(input('Ingrese un numero'))
m = int(input('Ingrese otro numero'))
#Argumentos POSICIONALES
funcion_resta(m, n)

#Argumentos por KEYWORD
funcion_resta(b=m, a=n)


#funcion_resta(m, n, 3 ) #DA ERROR

def funcion_saludar(nombre, apellido, edad):
    print(f'Buenas tardes {nombre} {apellido} su edad es {edad}')
    
nombre = input('Ingrese su nombre\n')
apellido = input('Ingrese su apellido\n')
edad = int(input('Ingrese su edad\n'))

funcion_saludar(apellido, nombre, edad)
funcion_saludar(apellido=apellido, nombre=nombre, edad=edad)

#funcion_saludar(apellido, nombre=nombre, edad=edad) ERROR se envian multiples datos a nombre

funcion_saludar(apellido, edad=nombre, apellido=edad)

#UNICA REGLA 
#Debe haber siempre un argumento por keyword a la derecha de uno ya declarado
#funcion_saludar(apellido=apellido, nombre, edad) #ERROR
#funcion_saludar(apellido, nombre=nombre, edad) #ERROR

