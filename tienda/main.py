# Creacion de listas
tienda = []
ventas = []

import os

def buscar_productos(nombre): # nombre = 'Tv'
    for p in tienda: # [p1, p2] => p1 = {'nombre':'Tv', 'precio': 500000}, p2 = {'nombre':'Lavadora', 'precio': 400000}
        if nombre == p['nombre']:
            return p # Econtramos producto
    return None # No encontramos producto

while True:
    os.system('cls')
    print('==== Menu de acciones ====')
    print('1. Agregar')
    print('2. Modificar')
    print('3. Eliminar')
    print('4. Mostrar')
    print('5. Vender')
    print('6. Total')
    
    print('0. Salir')
    
    opcion = input('Ingrese una opcion\n')
    
    os.system('cls')
    
    if opcion == '1':
        print('==== Agregar productos ====')
        nombre = input('Ingrese nombre de producto:\n').capitalize()
        respuesta = buscar_productos(nombre) # respuesta puede ser None o un Diccionario
        if respuesta is None:        
            precio = int(input('Ingrese precio de producto:\n'))
            producto = {'nombre':nombre, 'precio':precio}
            # Agregando producto a tienda
            tienda.append(producto)
            # Mensaje confirmacion
            print('Producto agregado')
        else:
            print('Producto ya existe')
        
    elif opcion == '2':
        print('==== Modificar producto ====')
        nombre = input('Ingrese nombre producto a buscar:\n').capitalize()
        respuesta = buscar_productos(nombre) # Retornamos None o un Diccionario
        if respuesta is not None:
            nuevo_precio = int(input('Ingrese nuevo precio de producto:\n'))
            # respuesta es un diccionario {'nombre':'Tv', 'precio':5000}
            respuesta['precio'] = nuevo_precio # Modificando precio de diccionario escogido
            print('Producto modificado')
        else:
            print('No se encontro producto a buscar')
    elif opcion == '3':
        print('==== Eliminar producto ====')
        nombre = input('Ingrese nombre producto a eliminar:\n').capitalize()
        respuesta = buscar_productos(nombre)
        if respuesta is not None:
            confirmacion = input('Desea eliminar el producto? Si/No').capitalize()
            if confirmacion == 'Si':
                tienda.remove(respuesta) # Eliminando por valor
                print('Se elimino producto')
            else:
                print('No se elimino producto')
        else:
            print('Producto no encontrado')
    elif opcion == '4':
        print('==== Listar productos en tienda ====')
        if len(tienda) == 0:
            print('No hay productos aun')
        else:
            for p in tienda:
                print(f'Nombre: {p["nombre"]}')
                print(f'Precio: {p["precio"]}')
                print('-----------------------------------------')
                
    elif opcion == '5':
        print('==== Vender productos ====')
        nombre = input('Ingrese nombre producto a vender:\n').capitalize()
        respuesta = buscar_productos(nombre)
        if respuesta is not None:
            # Copiar producto a ventas
            copia = respuesta.copy()
            ventas.append(copia)
            print('Producto vendido')
        else:
            print('Producto no encontrado')
    elif opcion == '6':
        print('==== Total ventas ====')
        total = 0
        if len(ventas) == 0:
            print('No hay ventas aun')
        else:
            for v in ventas:
                print(f'{v["nombre"]}..................{v["precio"]}')
                total += v['precio']
            print('__________________________')
            print(f'Total..................{total}')
    elif opcion == '0':
        print('Saliendo programa')
        break
    else:
        print('Opcion ingresada no valida')
        
    input('Presione enter para continuar...')