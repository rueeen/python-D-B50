'''
4

*
**
***
****
'''
n = int(input('Ingrese tamaño triangulo\n'))

print("dificil")
#forma dificil while or for
for i in range(1, n + 1):
    for j in range(i):
        print('*', end="")
    print()
        
print("facil")
#forma facil
for i in range(1, n + 1):
    print('*' * i)