# Menu de acciones para CRUD -> Create Read Update Delete

# Creamos lista fuera del menu
lista_nombres = []

# Menu
while True:    
    print('==== Menu de opciones ====')
    print('1. Agregar a lista C')
    print('2. Mostrar lista R')
    print('3. actualizar lista U')
    print('4. Eliminar elemto lista D')
    print('0. Salir')
    
    opcion = input('Ingrese su opcion\n')
    
    if opcion == '0':
        print('Saliendo de programa...')
        break
    
    elif opcion == '1':
        print('==== Agregar elemento a lista ====')
        nombre = input('Ingrese un nombre\n')
        #Agrear algo a la lista con metodo .append()
       
        lista_nombres.append(nombre) # Esto agrega el nombre ingresado a la lista
        # lista_nombres.insert(2, nombre) # Agrega en el indice 2 de la lisast el nombre
        print(f'Se agrego {nombre} a la lista')
        
    elif opcion == '2':
        print('==== Listado Nombres ====')
        if len(lista_nombres) == 0:
            print('Lista vacia')
        else:
            for i in lista_nombres:
                print(i)
        
    elif opcion == '3':
        print('==== Modificando lista ====')
        # Para modificar necesitamos 2 cosas
        # indice del elemento a modificar, nuevo valor
        # RECORRIENDO LISTA POR INDICES
        for i in range(len(lista_nombres)):
            print(f'Nombre: {lista_nombres[i]} -> Indice: {i}')
            
        # Los indices deben ser NUMERICOS ENTEROS
        indice = int(input('Ingrese indice a modificar\n'))
        # Nuevo nombre
        nuevo_nombre = input('Ingrese nombre a modificar\n')
        # Modificamos de la siguiente manera
        lista_nombres[indice] = nuevo_nombre
        print('Se modifico nombre')
        
    elif opcion == '4':
        print('==== Eliminando datos ====')
        # Para eliminar necesito el indice del elemento
        # RECORRIENDO LISTA POR INDICES
        for i in range(len(lista_nombres)):
            print(f'Nombre: {lista_nombres[i]} -> Indice: {i}')
            
        indice = int(input('Ingrese indice a eliminar\n'))
        
        # Para eliminar usamos metodo .pop()
        
        eliminado = lista_nombres.pop(indice) # .pop() ademas retorna el valor eliminado
        # del lista_nombres[indice] # Eliminando con del
        print(f'Se elimino {eliminado} y la lista quedo como {lista_nombres}')