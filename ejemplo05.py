#Sumar 2 numeros ingresados desde consola
numero1 = input("Ingrese 2 numeros\n") #tipo str
numero2 = int(input("Ingrese 2 numeros\n")) #tipo str
#input siempre SIEMPRE retorna el valor ingresado como string

#Para convertir a ENTERO uso la funcion int()
print(type(int(numero1)))
nuevo_numer1 = int(numero1)

sumar = nuevo_numer1 + numero2

print("Resultado es igual a", sumar)
