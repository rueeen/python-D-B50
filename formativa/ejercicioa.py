'''
a.	Cree una función en python que reciba un día, mes y año. Debe retornar 
True si la fecha es correcta o False si no lo es. Considere años bisiestos. 
'''

#Mi funcion recibe un dia mes y año
def validar_fecha(dia, mes, anio):
    if anio >= 1 and anio <= 2024:
        #Considerando meses con 30 dias
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia >= 1 and dia <= 30:
                return True
        #Considerando meses con 31 dias
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia >= 1 and dia <= 31:
                return True
        elif mes == 2:
            if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
                if dia >= 1 and dia <= 29:
                    return True
            else:
                if dia >= 1 and dia <= 28:
                    return True
        else:
            return False
    else:
        return False
        print('No se ejecuta')

d = int(input("Ingrese dia de nacimiento\n"))
m = int(input("Ingrese mes de nacimiento\n"))
a = int(input("Ingrese año de nacimiento\n"))
#respuesta sera True o False
respuesta = validar_fecha(d, m, a)

if respuesta == True:
    print(f"La fecha {d}/{m}/{a} es valida")
else:    
    print(f"La fecha {d}/{m}/{a} es invalida")