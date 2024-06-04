'''
Requerimientos agenda
1. Mi agenda debe registrar personas con nombre, apellido y numero telofono. C
2. Mi agenda debe mostrar el listado de personas con nombre, apellido y telefeno. R
3. Mi agenda debe permitir modificar el numero de telefono por nombre y apellido. U
4. Mi agenda debe permitir eliminar contactos por nombre y apellido. D
'''
# Para limpiar pantalla utilizaremos el modulo OS
import os # Permite interactuar con sistema operativo 

# Funcion para buscar un contacto
def buscar_contacto(nombre, apellido, lista):
    for c in lista:
        if nombre == c['nombre'] and apellido == c['apellido']:
            # Encontramos el contacto
            return c
    return None # Retorna None

agenda = [] # Lista vacia para guardar contactos
while True: # Ciclo repetitivo para realizar diferentes acciones
    os.system('cls') # Ejecuta comando cls para limpiar terminal
    print('==== Menu de opciones ====')
    print('1. Agregar contacto')
    print('2. Mostrar contactos')
    print('3. Actualizar datos contacto')
    print('4. Eliminar contacto')
    print('0. Salir')
    
    opcion = input('Ingrese la opcion a realizar\n') # Opcion a realizar
    os.system('cls')
    if opcion == '1': 
        print('==== Crear contacto ====')
        nombre = input('Ingrese nombre contacto\n').capitalize().strip() # " hola " -> "hola"
        apellido = input('Ingrese apellido contacto\n').capitalize().strip() # "   " -> ""
        if nombre == '' or apellido == '':
            print('Nombre y/o apellido vacios')
        else:
            try:
                telefono = int(input('Ingrese telefono contacto\n'))
                #Invocamos funcion
                respuesta = buscar_contacto(nombre, apellido, agenda)
                if respuesta is None:
                    contacto = {'nombre':nombre, 'apellido':apellido, 'telefono':telefono}
                    agenda.append(contacto)
                    print(f'Se agrego contacto {nombre} {apellido}')
                else:
                    print('Contacto ya se encuentra registrado')
            except:
                print('No se pueden agregar telefonos con letras')
        
    elif opcion == '2':
        print('==== Lista contactos ====')
        if len(agenda) == 0:
            print('No hay contactos aun')
        else:
            print('1. Mostrar todos')
            print('2. Mostrar por apellido')
            print('3. Mostrar uno')
            
            opcion = input('Ingrese su opcion:\n')
            
            if opcion == '1':
                for c in agenda: # c representa un diccionario con keys nombre, apellido, telefono
                    print(f'Nombre: {c["nombre"]}')
                    print(f'Apellido: {c["apellido"]}')
                    print(f'Telefono: {c["telefono"]}')
                    print('-----------------------------------')
                    
            elif opcion == '2':
                apellido = input('Ingrese apellido a buscar\n').capitalize().strip()
                
                for c in agenda: # c representa un diccionario con keys nombre, apellido, telefono
                    if c['apellido'] == apellido:
                        print(f'Nombre: {c["nombre"]}')
                        print(f'Apellido: {c["apellido"]}')
                        print(f'Telefono: {c["telefono"]}')
                        print('-----------------------------------')
                        
            elif opcion == '3':
                nombre = input('Ingrese nombre a buscar\n').capitalize().strip()
                apellido = input('Ingrese apellido a buscar\n').capitalize().strip()
                
                contacto = buscar_contacto(nombre, apellido, agenda)
                
                print(f'Nombre: {contacto["nombre"]}')
                print(f'Apellido: {contacto["apellido"]}')
                print(f'Telefono: {contacto["telefono"]}')
                print('-----------------------------------')
        
    elif opcion == '3':
        print('==== Modificar Contacto ====')
        nombre = input('Ingrese nombre a modificar\n').capitalize().strip()
        apellido = input('Ingrese apellido a modificar\n').capitalize().strip()
        
        if nombre == '' or apellido == '':
            print('Nombre y/o apellido vacios')
        else:        
            respuesta = buscar_contacto(nombre, apellido, agenda)
            
            if respuesta is not None:
                try:
                    nuevo_telefono = int(input('Ingrese nuevo numero\n'))
                    respuesta['telefono'] = nuevo_telefono
                    print('Se ha modificado contacto')
                except:
                    print('No se pueden agregar telefonos con letras')
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
            
    elif opcion == '0':
        print('Saliendo programa...')
        break
    else:
        print('Opcion ingresada no valida')
    
    input('Presione enter para continuar...')
        