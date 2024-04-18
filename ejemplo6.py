# Recibir una calle y un numero e imprimir por pantalla
# "Su direccion es {calle}, {numero}" 

calle = input('Ingrese su calle\n')
numero = int(input('Ingrese su numero de casa\n'))#\n salto de linea

#solucion sencilla
print("Su direccion es calle", calle,",", numero)

#solucion 2 concatenar
nueva_frase = "Su direccion es calle "+calle+", "+str(numero) 
#Error no se puede usar operador + entre str y int
print(nueva_frase)

#Solucion 3 format str
print(f'Su direccion es calle {calle}, {numero}')
