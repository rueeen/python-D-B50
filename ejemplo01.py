# funcion print
# es un comentario
# print es una funcion

print("Lo que queremos mostrar por consola")

# "Su edad es: ", variable

edad = 20
print("Su edad es: ", edad)
print("Su edad es:", edad)
# print("Su edad es:" edad) esto da erro de sintaxis por la coma omitida

#Ejemplo sep, sep es OPCIONAL
print("Su edad es", edad, sep="/")
# print("Su edad es", edad, sep=2) da error porque sep acepta solo CARACTERES (STR)

#ejemplo end, end es OPCIONAL, por defecto es un \n (Salto de linea)
print("hola", end=' ')
print("alumnos", end='final') #end solo acepta strings como valor
print('2024')

