#Ejemplo for

#Estructura
# for  variable_control in elemento_iterable :
# Vamos a conocer 2 elementos iterables
print('Recorriendo str')
for i in 'Hola mundo':  #str
    print(i)
# range de entero
# range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print('Recorriendo range(int)')
for j in range(10):
    print(j)
    
# segunda forma del range
# range(2, 10) 2 es el inicio, 10 el fin - 1
# 2, 3, 4, 5, 6, 7, 8, 9 
for j in range(2, 10):
    print(j)
# el primero debe ser menor que el segundo, si no queda una lista vacia
for j in range(20, 10):
    print(j)
    
#Tercera forma de range
# range(2, 10, 2) 2 es el inicio, 10 - 1 el fin, 2 es el incremento
# 2, 4, 6, 8
for k in range(2, 10, 2):
    print(k)
# 20, 19, 18, 17, 16, 15, 14, 13, 12, 11
for k in range(20, 10, -1):
    print(k)