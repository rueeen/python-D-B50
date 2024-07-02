import os

def buscar_cuentas(rut):
    for c in banco:
        if c['rut'] == rut:
            return c
    return None

banco = [] # 1 punto

while True:
    os.system('cls')
    print('==== Menu de opciones ====')
    print('1. Agregar clientes')
    print('2. Realizar deposito')
    print('3. Realizar giro')
    print('4. Mostrar cuentas')
    print('0. Salir')
    
    opcion = input('Ingrese su opcion\n')
    os.system('cls')
    if opcion == '1':
        
        rut = input('Ingrese su rut:\n')
        cliente = buscar_cuentas(rut)
        if cliente is None:
            nombre = input('Ingrese su nombre:\n').capitalize()
            cliente = {'rut':rut, 'nombre':nombre, 'monto':0}
            banco.append(cliente)
            print('Cliente agregado.')
        else:
            print('Rut ya existe.')
    elif opcion == '2':
        print('==== Realizar deposito ====')
        rut = input('Ingrese su rut a depositar:\n')
        cliente = buscar_cuentas(rut)
        if cliente is None:
            print('Rut no encontrado')
        else:
            try:
                monto = int(input('Ingrese monto a depositar:\n'))
            except:
                print('Monto ingresado no corresponde a numeros')
                input('Presione enter para continuar...')
                continue
            if monto >= 500 and monto <= 1000000:
                cliente['monto'] += monto
                print(f'Se realizo un deposito de {monto}')
            else:
                print('Monto ingresado debe estar entre 500 y 1000000')
                
    elif opcion == '3':
        print('==== Realizar giro ====')
        rut = input('Ingrese su rut a girar:\n')
        cliente = buscar_cuentas(rut)
        if cliente is None:
            print('Rut no encontrado')
        else:
            try:
                monto = int(input('Ingrese monto a girar:\n'))
            except:
                print('Monto ingresado no corresponde a numeros')
                input('Presione enter para continuar...')
                continue
            if monto >= 0 and monto <= cliente['monto']:
                cliente['monto'] -= monto
                print(f'Se realizo un giro de {monto}')
            else:
                print('La cuenta no tiene el monto suficiente')
        
    elif opcion == '4':
        print('==== Lista cuentas ====')
        if len(banco) == 0:
            print('No hay cuentas actualmente')
        else:
            for c in banco:
                print(f'Rut: {c["rut"]}')                
                print(f'Nombre: {c["nombre"]}')
                print(f'Monto: {c["monto"]}')
                print('----------------------------')
                
    elif opcion == '0':
        print('Saliendo programa...')
        break
    
    else:
        print('Opcion ingresada no valida')
    input('Presione enter para continuar...')
    
    