def mostrar_menu():
    print("Menú")
    print("1.Guardar producto")
    print("2.Mostrar producto")
    print("3.Actualizar producto")
    print("4.Editar producto")
    print("5.Eliminar producto")
    print("6.Salir")

def mostrar_opt():
    validar_opt = False
    while not validar_opt:
        try:
            opcion = int(input("Ingrese una opción del 1 al 6 (numero entero): "))
            if 1 <= opcion <= 6:
                validar_opt = True
            else:
                print("Error: opción fuera de rango")
        except ValueError:
            print("Error: Ingrese un dato valido (numero entero)")
    return opcion

opt = mostrar_opt