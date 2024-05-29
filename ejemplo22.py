# diccionario

personas = {'222-2': 'Ruben Valencia', '222-2': 'Perico los palotes'}

print(personas['222-2'])

# modificar
personas['222-2'] = 'Ruben Valencia'
personas['111-1'] = 'Maria las petunias' #Esto crea una nueva key porque no existe

print(personas)

# eliminar
del personas['111-1'] # Esto elimina a Maria las petunias
personas.pop()
