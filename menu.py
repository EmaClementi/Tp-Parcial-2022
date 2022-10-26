from gestionCanciones import *
verListaCanciones()
opciones = input("Ingrese una opcion:(Listar Canciones)(Buscar Cancion)(Agregar Cancion)(Modificar Cancion)(Salir):").lower()

def menu(opciones):
    while opciones != "salir":
        if opciones == "listar canciones":
            opcion = input("Desea listar por: (Nombre)(Artista)(Letra)?:").lower()
            filtrarCanciones(opcion)
        elif opciones == "buscar cancion":
            cancion = input("Ingrese el Nombre de la Cancion que desea encontrar:").upper()
            buscarCancion(cancion)
        elif opciones == "agregar cancion":
            agregarCancion()
        elif opciones == "modificar cancion":
            cancion = input("Ingrese el Nombre de la Cancion que desea modificar:").upper()
            modificarCancion(cancion)
        else:
            print("La opcion ingresada no es correcta")

        opciones = input("Ingrese una opcion:(Listar Canciones)(Buscar Cancion)(Agregar Cancion)(Modificar Cancion)(Salir):").lower() 
         
menu(opciones)
