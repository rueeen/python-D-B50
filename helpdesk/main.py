# Funcion para buscar un contacto
def buscar_ticket(codigo, lista):
    for c in lista:
        if codigo == c['codigo']:
            # Encontramos el ticket
            return c # es un diccionario con keys codigo y titulo
    return None # Retorna None

# Listas
tickets_abiertos = []
tickets_cerrados = [] # 1 punto

while True:
    print('==== Menu de opciones ====')
    print('1. Crear ticket')
    print('2. Cerrar ticket')
    print('3. Eliminar tickets cerrados')
    print('4. Listar tickets abiertos')
    print('5. Listar tickets cerrados')
    print('0. Salir')
    
    opcion = input('Ingrese la opcion a realizar:\n')
    
    if opcion == '1':
        print('==== Crer ticket ====')
        c = input('Ingrese un codigo:\n')
        t = input('Ingrese un titulo:\n')
        
        if len(c) > 4 or c.strip() == '': # " hola mundo    " -> "hola mundo"
            print('El codigo no puede superar los 4 caracteres y/o no puede ser vacio')
        else:
            ticket = {'codigo':c, 'titulo': t} # Creando diccionario   
            tickets_abiertos.append(ticket) # Agregando diccionario a lista
            print(f'Se ha creado el ticket con codigo {c}')   
        
    elif opcion == '2':
        print('==== Cerrando ticket ====')
        # Buscar el ticket correspondiente al codigo ingresado.
        codigo = input('Ingrese codigo de ticket a buscar:\n') # Ingresamos el codigo del ticket a buscar
        t = buscar_ticket(codigo, tickets_abiertos) # Retorna None o Diccionario ticket
        if t is not None:
            # t es un diccionario
            # Si lo encuentra, solicitar un comentario por consola y 
            # añadirlo con una nueva clave al diccionario encontrado.
            comentario = input('Ingrese un comentario:\n')
            t['comentario'] = comentario # Creamos nueva clave comentario con el valor ingresado
            # Añadir el diccionario modificado con la nueva clave a la lista “tickets_cerrados”.
            tickets_cerrados.append(t)
            # Eliminar el diccionario modificado de la lista “tickets_abiertos”.
            tickets_abiertos.remove(t)
            print('Ticket cerrado')            
        else:
            print('Ticket no encontrado')       
        
    elif opcion == '3':
        print('==== Limpiando lista ticket cerrados ====')
        respuesta = input('Esta seguro que desea eliminar los ticket cerrados? si/no').lower()
        
        if respuesta == 'si':
            tickets_cerrados.clear() # VACIA LA LISTA
            print('Se eliminaron los ticket')
        else:
            print('Se mantiene la lista')
    elif opcion == '4':
        print('==== Listar ticket abiertos ====')
        if len(tickets_abiertos) == 0:
            print('No hay tickets abiertos')
        else:
            for t in tickets_abiertos:
                print(f'Codigo: {t["codigo"]}')
                print(f'Titulo: {t["titulo"]}')
                print('---------------------------------')
    elif opcion == '5':
        print('==== Listar ticket cerrados ====')
        if len(tickets_cerrados) == 0:
            print('No hay tickets cerrados')
        else:
            for t in tickets_cerrados:
                print(f'Codigo: {t["codigo"]}')
                print(f'Titulo: {t["titulo"]}')
                print(f'Comentarios: {t["comentario"]}')
                print('---------------------------------')
    elif opcion == '0':
        print('Saliendo programa...')
        break # 1 punto
    else:
        print('Debe seleccionar una opcion valida') # 1 punto