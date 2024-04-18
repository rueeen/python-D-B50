#if elif else

a = int(input("Ingrese un numero\n"))
b = int(input("Ingrese un numero\n"))

if a > b:
    print(f'El mayor es {a}')
elif a < b:
    print(f'El mayor es {b}')
else:
    print("Son iguales")