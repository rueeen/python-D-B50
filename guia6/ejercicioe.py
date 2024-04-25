n = int(input('Ingrese un numero positivo\n'))
#Mientras el numero sea 0 o negativo se volver a solicitar
while n <= 0:
    print('Error: Debe ingresar un numero positivo')
    #Solicitamos el numero nuevamente    
    n = int(input('Intente nuevamente\n'))
    
for i in range(n, -1, -1):
    final = ', '
    
    if i == 0:
        final= '\n'
        
    print(i, end=final)