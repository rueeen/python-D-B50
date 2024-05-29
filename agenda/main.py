'''
Requerimientos agenda
1. Mi agenda debe registrar personas con nombre, apellido y numero telofono. C
2. Mi agenda debe mostrar el listado de personas con nombre, apellido y telefeno. R
3. Mi agenda debe permitir modificar el numero de telefono por nombre y apellido. U
4. Mi agenda debe permitir eliminar contactos por nombre y apellido. D
'''

# Funcion para buscar un contacto
def buscar_contacto(nombre, apellido, lista):
    for c in lista:
        if nombre == c['nombre'] and apellido == c['apellido']:
            # Encontramos el contacto
            return c
    return None # Retorna None

agenda = [] # Lista vacia para guardar contactos
while True: # Ciclo repetitivo para realizar diferentes acciones
    print('==== Menu de opciones ====')
    print('1. Agregar contacto')
    print('2. Mostrar contactos')
    print('3. Actualizar datos contacto')
    print('4. Eliminar contacto')
    print('0. Salir')
    
    opcion = input('Ingrese la opcion a realizar\n') # Opcion a realizar
    
    if opcion == '1': 
        print('==== Crear contacto ====')
        nombre = input('Ingrese nombre contacto\n').capitalize()
        apellido = input('Ingrese apellido contacto\n').capitalize()
        telefono = int(input('Ingrese telefono contacto\n'))
        #Invocamos funcion
        respuesta = buscar_contacto(nombre, apellido, agenda)
        if respuesta is None:
            contacto = {'nombre':nombre, 'apellido':apellido, 'telefono':telefono}
            agenda.append(contacto)
            print(f'Se agrego contacto {nombre} {apellido}')
        else:
            print('Contacto ya se encuentra registrado')
        
    elif opcion == '2':
        print('==== Lista contactos ====')
        if len(agenda) == 0:
            print('No hay contactos aun')
        else:
            for c in agenda: # c representa un diccionario con keys nombre, apellido, telefono
                print(f'Nombre: {c["nombre"]}')
                print(f'Apellido: {c["apellido"]}')
                print(f'Telefono: {c["telefono"]}')
                print('-----------------------------------')
        
    elif opcion == '3':
        print('==== Modificar Contacto ====')
        nombre = input('Ingrese nombre a modificar\n').capitalize()
        apellido = input('Ingrese apellido a modificar\n').capitalize()
        
        respuesta = buscar_contacto(nombre, apellido, agenda)
        
        if respuesta is not None:
            nuevo_telefono = int(input('Ingrese nuevo numero\n'))
            respuesta['telefono'] = nuevo_telefono
            print('Se ha modificado contacto')
        else:
            print('No se encontro contacto')
            
    elif opcion == '4':
        print('==== Eliminar contacto ====')
        nombre = input('Ingrese nombre a eliminar\n').capitalize()
        apellido = input('Ingrese apellido a eliminar\n').capitalize()
        
        respuesta = buscar_contacto(nombre, apellido, agenda)
        
        if respuesta is not None:
            # respuesta es un diccionario con keys nombre, apellido, telefono
            agenda.remove(respuesta)
            print('Se elimino contacto')
        else:
            print('No se encontro contacto a eliminar')
        
        