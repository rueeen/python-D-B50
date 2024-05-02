#Funciones sin retorno

v = print('Hola')
print(v) #None -> Ausencia de valor

#Funciones con retorno

v = input('Hola')
print(v) #aca depende de lo ingresado por el usuario y es de tipo str

#Definiendo funciones co retorno
def sumaNumeros(a, b):
    resultado = a + b
    return resultado

r = sumaNumeros(3, 5) # r recibe el valor retornado, que es la suma de a y b

print(r)

def validarCaracteres(valor):
    #validamos que tenga 8 caracteres
    #valor -> saludo
    if len(valor) == 8:
        return True #retorna True
    
    return #retorna None

v = input('Ingrese un valor')

r = validarCaracteres(v)

if r == True:
    print('Valor valido')
else:
    print('Valor invalido')
    
def ciclo():
    for i in range(10):
        if i == 3:
            return i # retorna 3
            print('No se ejecuta') #El retorno termina la ejecucion de un ciclo y de la funcion, volviendo a la linea 44 donde se invoco         
    
        
r = ciclo() # r = 3 
print(r)