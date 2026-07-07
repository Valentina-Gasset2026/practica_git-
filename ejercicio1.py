print("Saludo 1 otra vez")
print("Saludo extra")
print("saludoooooooooo")
print("Practica código")

def menu_opciones():
    print("1.Guardar peli")
    print("2.Mostrar peli")
    print("3.Salir")


def mostrar_opciones():
    validacion_opcion = False
    while validacion_opcion == False:
        try:
            opcion = int(input("Ingrese una opcion (1-3): "))
            if opcion >= 1 and opcion <= 3:
                validacion_opcion = True
            else:
                print("Error: ingrese una opción entre 1 y 3")
        except ValueError:
            print("Error: Ingrese un dato valido, como por ejemplo un mumero entero")
    return opcion

#opt = mostrar_opciones()

def mostrar_nombre():
    validar_nombre = False
    while validar_nombre == False:
        nombre_peli = input("ingrese nombre de la pelicula: ")
        if nombre_peli == "":
            print("Error: no se aceptan vacíos")
        else:
            validar_nombre = True
    return nombre_peli

nombre = mostrar_nombre()

peliculas = [
    {
        
    }
]

activo = False
while activo == False:
    menu_opciones()
    opt = mostrar_opciones()
    if opt == 1:
        print("Guardar peli")
    elif opt == 2:
        print("Mostrar")
    else:
        activo = True