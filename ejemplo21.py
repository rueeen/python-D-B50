

personas = [] #Una lista
while True:
    print('1. Agregar nombre')
    print('2. Mostrar personas')
    print('3. Eliminar nombre')
    
    opcion = input('Ingrese un nuevo nombre\n')
    
    if opcion == '1':
        nombre = input('Ingrese un nombre\n')
        edad = int(input('Ingrese una edad\n'))
        
        dato_persona = {'nombre':nombre, 'edad':edad}
        personas.append(dato_persona)
    
    elif opcion == '2':
        if len(personas) == 0:
            print('No hay personas en la lista')
        else:
            # Recorriendo por valor
            for p in personas:
                # print(p) # es un diccionario
                print(f'Nombre: {p["nombre"]}')
                print(f'Edad: {p["edad"]}')
                print('-------------------------')