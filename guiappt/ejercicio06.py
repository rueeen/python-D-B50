'''
Solicitar al usuario un número y un porcentaje, para mostrar por 
pantalla el número correspondiente al porcentaje del número ingresado
'''

numero = int(input("Ingrese un numero\n"))
porcentaje = int(input("Ingrese un porcentaje\n"))

resultado = numero * porcentaje / 100

print(f'El {porcentaje}% de {numero} es {resultado}')