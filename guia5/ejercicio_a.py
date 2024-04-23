#Solicitamos datos de entrada
#Convertimos los datos de str a float
peso = float(input('Ingrese su peso\n'))
altura = float(input('Ingrese su altura\n'))

#Proceso
imc = peso / (altura * altura)

#comparacion 
if imc <= 15:
    print('Delgadez muy severa.')
elif imc > 15 and imc <= 15.9:
    print('Delgadez severa.')
elif imc <= 18.4:
    print('Delgadez.')
elif imc <= 24.9:
    print('Peso saludable')
    
#Aqui van las otras opciones  
    
else:
    print('Obesidad muy severa')