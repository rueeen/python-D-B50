#SCOPE
nombre = "Perico"

def cambiarNombre(nombre):
    nombre = 'Maria'
    print(nombre)
    
cambiarNombre(nombre)

print(nombre) #imprime Perico porque nombre dentro de funcion esta en el contexto interno de la funcion