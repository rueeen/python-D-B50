#Ejemplo WHILE

a = 10

#Estructura while
# while  condicion  :
while a < 10 :
    print('Esto nunca se ejecuta')

#Esto es infinito
#while a > 0:
#    print('Se ejecuta')

while a > 0:
    print('Se ejecuta')
    a -= 1
print('Fuera del ciclo')

#Deseo que se ingrese un numero positivo por input
n = int(input('Ingrese un numero positivo\n'))

while n <= 0:
    n = int(input('Error, debe ser un positivo. Intente nuevamente\n'))
    
print('Fuera del ciclo')