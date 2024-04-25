# Dato entrada => 10
# Dato salida  => 1, 3, 5, 7, 9

n = int(input('Ingrese un numero positivo\n'))
#Mientras el numero sea 0 o negativo se volver a solicitar
while n <= 0:
    print('Error: Debe ingresar un numero positivo')
    #Solicitamos el numero nuevamente    
    n = int(input('Intente nuevamente\n'))
    
for i in range(n+1):
    final = ", "
    if i == n or i == n - 1:
        final = "\n"
    if i % 2 != 0:
        print(i, end=final)