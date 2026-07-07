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

def mostrar_nombre_producto():
    validar_nombre = False
    while not validar_nombre:
        nombre_producto = input("Ingrese nombre: ").strip().lower()
        if nombre_producto == "":
            print("Error, nombre no puede ir vacio")
        else:
            validar_nombre = True
            break 
    return nombre_producto

nombre = mostrar_nombre_producto()
opt = mostrar_opt

def mostrar_stock():
    validar_stock = False
    while not validar_stock:
        try:
            cantidad_stock = int(input("Ingrese la cantidad de stock: "))
            if cantidad_stock >= 0 and cantidad_stock <= 500:
                validar_stock = True
                break 
            else:
                print("Error, ingrese una cantidad entre 0 y 500")
        except ValueError:
            print("Error, ingrese un valor valido (numero entero)")
    return cantidad_stock

stock = mostrar_stock()

def mostrar_precio():
    validar_precio = False
    while not validar_precio:
        try:
            precio_producto = float(input("Ingrese el precio del producto: "))
            if precio_producto > 0 :
                validar_precio = True
                break 
            else:
                print("Error: ingrese un numero mayor que 0")
        except ValueError:
            print("Error: Ingrese un numero decimal")
    return precio_producto

precio = mostrar_precio()



productos = []
productos_disponibles = 500

