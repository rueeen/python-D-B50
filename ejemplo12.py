#Ejemplo break

while True:
    resp = input('Desea terminar? si/no\n').lower()
    
    if resp == 'si':
        break #break rompe el ciclo independientemente de si quedan cosas por recorrer
        print('Esto no se ejecuta')
    
    print('continuando')
    
print('fuera del ciclo')

#Ejemplo continue

for i in range(5):
    if i == 3:
        continue #continue cuando se ejecuta salta del ciclo actual al siguiente
    print(i)