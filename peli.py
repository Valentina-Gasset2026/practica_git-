def mostrar_menu():
    print("#####[Peliculas]#####")
    print("1.Guardar peliculas")
    print("2.Mostrar peliculas") # Que se vea los estados actualizados
    print("3.Buscar peliculas")
    print("4.Editar peliculas")
    print("5.Eliminar peliculas")
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

def mostrar_nombre_peli():
    validar_nombre = False
    while not validar_nombre:
        nombre_peli = input("Ingrese el nombre de la pelicula: ").strip().lower()
        if nombre_peli == "":
            print("Error, el nombre de la pelicula no puede ir vacio")
        else:
            validar_nombre = True
    return nombre_peli

def mostrar_año_pelicula():
    validar_año = False
    while not validar_año:
        try:
            año_pelicula = int(input("Ingrese el año de la pelicula: "))
            if año_pelicula >= 0:
                validar_año = True
            else:
                print("Error: Ingrese un año valido (mayor o igual a 0)")
        except ValueError:
            print("Error: Ingrese un dato valido (numero entero)")
    return año_pelicula

def mostrar_categoria():
    categoria_peli = input("Ingrese la categoria de la pelicula: ").strip().lower()
    while categoria_peli == "":
        print("Error: la categoria de la pelicula no puede ir en blanco")
        categoria_peli = input("Ingrese nuevamente la categoria de la pelicula: ").strip().lower()
    return categoria_peli

def mostrar_reparto_peli():
    validar_reparto = False
    while not validar_reparto:
        reparto_peli = input("Ingrese el reparto de la pelicula: ").strip().lower()
        if reparto_peli == "":
            print("Error: El reparto de la pelicula no puede ir en blanco")
        else:
            validar_reparto = True
    return reparto_peli

def guardar_pelicula(peliculas):
    nombre = mostrar_nombre_peli()
    año = mostrar_año_pelicula()
    categoria = mostrar_categoria()
    reparto = mostrar_reparto_peli()

    nueva_peli = {
        "nombre": nombre,
        "año": año,
        "categoria": categoria,
        "reparto": reparto,
    }
    peliculas.append(nueva_peli)
    print("Pelicula guardada con exito")

def buscar_peliculas(peliculas):
    pelicula_a_buscar = input("Ingrese el nombre de la pelicula que desee buscar: ").strip().lower()
    while pelicula_a_buscar == "":
        print("Error: el nombre no puede estar vacio")
        pelicula_a_buscar = input("Ingrese el nombre de la pelicula que desee buscar: ").strip().lower()
    
    encontrada = False
    for posicion, pelicula in enumerate(peliculas):
        if pelicula_a_buscar == pelicula['nombre']:
            print("Pelicula encontrada")
            print(f"{posicion+1} - {pelicula['nombre'].title()} ({pelicula['año']}) - {pelicula['categoria'].title()} - Reparto: {pelicula['reparto']}")
            encontrada = True
            break
    if not encontrada:
        print("Pelicula NO encontrada")
    return pelicula_a_buscar

def editar_pelicula(peliculas):
    if not peliculas:
        print("No hay peliculas para editar")
        return
    
    pelicula_a_editar = input("Ingrese el nombre de la pelicula a editar: ").strip().lower()
    while pelicula_a_editar == "":
        print("Error: el nombre no puede estar vacio")
        pelicula_a_editar = input("Ingrese el nombre de la pelicula a editar: ").strip().lower()
    
    for posicion, pelicula in enumerate(peliculas):
        if pelicula_a_editar == pelicula['nombre']:
            print(f"Editando: {pelicula['nombre'].title()}")
            print("Deje en blanco para no modificar el campo.")
            
            nuevo_nombre = input(f"Nuevo nombre (actual: {pelicula['nombre']}): ").strip().lower()
            if nuevo_nombre != "":
                pelicula['nombre'] = nuevo_nombre
            
            nuevo_año = input(f"Nuevo año (actual: {pelicula['año']}): ").strip()
            if nuevo_año != "":
                try:
                    nuevo_año_int = int(nuevo_año)
                    if nuevo_año_int >= 0:
                        pelicula['año'] = nuevo_año_int
                    else:
                        print("Año no válido, se mantiene el anterior")
                except ValueError:
                    print("Año no válido, se mantiene el anterior")
            
            nueva_categoria = input(f"Nueva categoria (actual: {pelicula['categoria']}): ").strip().lower()
            if nueva_categoria != "":
                pelicula['categoria'] = nueva_categoria
            
            nuevo_reparto = input(f"Nuevo reparto (actual: {pelicula['reparto']}): ").strip().lower()
            if nuevo_reparto != "":
                pelicula['reparto'] = nuevo_reparto
            
            print("Pelicula actualizada con exito")
            return
    print("Pelicula no encontrada")

def eliminar_pelicula(peliculas):
    if not peliculas:
        print("No hay peliculas para eliminar")
        return
    
    pelicula_a_eliminar = input("Ingrese el nombre de la pelicula a eliminar: ").strip().lower()
    while pelicula_a_eliminar == "":
        print("Error: el nombre no puede estar vacio")
        pelicula_a_eliminar = input("Ingrese el nombre de la pelicula a eliminar: ").strip().lower()
    
    for posicion, pelicula in enumerate(peliculas):
        if pelicula_a_eliminar == pelicula['nombre']:
            print(f"Eliminando: {pelicula['nombre'].title()}")
            del peliculas[posicion]
            print("Pelicula eliminada con exito")
            return
    print("Pelicula no encontrada")

def mostrar_peliculas(peliculas):
    if not peliculas:
        print("No hay peliculas guardadas")
        return
    for posicion, pelicula in enumerate(peliculas):
        print(f"{posicion+1}. {pelicula['nombre'].title()} ({pelicula['año']}) - {pelicula['categoria'].title()} - Reparto: {pelicula['reparto']}")

# Programa principal
peliculas = []  # Lista vacía inicialmente
activo = False
while not activo:
    mostrar_menu()
    opt = mostrar_opt()
    if opt == 1:
        print("Guardar")
        guardar_pelicula(peliculas)
    elif opt == 2:
        print("Mostrar peliculas")
        mostrar_peliculas(peliculas)
    elif opt == 3:
        print("Buscar")
        buscar_peliculas(peliculas)
    elif opt == 4:
        print("Editar")
        editar_pelicula(peliculas)
    elif opt == 5:
        print("Eliminar pelicula")
        eliminar_pelicula(peliculas)
    else:  # opt == 6
        print("Salir")
        activo = True