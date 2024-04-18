#Crear correo
#metodos de str
nombre = input("Ingrese su nombre\n").lower() #deja todo en minusculas
apellido = input("Ingrese su apellido\n").lower() #deja todo en minusculas

#1 forma mas correcta
correo = nombre + "." + apellido + "@correo.cl"
#metodo replace permite reemplazar caracteres por otro
correo_final = correo.replace(" ", "_")

print(f'Su correo es {correo_final}')

#2 forma limitada
print(f'Su correo es {nombre}.{apellido.replace(" ", "_")}@correo.cl')