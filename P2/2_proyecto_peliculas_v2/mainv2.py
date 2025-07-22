#Crear un proyecto  que permita  gestionar (administrar películas); colocar  un menu  de opciones para agregar, borrar,  modificar, consultar, buscar y vaciar películas 
#Notas: 
#1.-utiliza  funciones y mandar a llamar desde otro archivo 
#2.- Utilizar dict  para almacenar  los siguentes atrivutos (nombre, categoria, clasificacion, genero,idioama de la película, )

import Peliculas_V2

opcion=True
while opcion:
    Peliculas_V2.borra_pantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n\n 1.- Crear \n 2.- Borrar \n 3.- Mostrar \n 4.- Agregar una caracteristica  \n 5.- Modificar caracteristica \n 6.- Borrar Caracterisitca  \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            Peliculas_V2.crear_peliculas()
            Peliculas_V2.esperarTecla()
        case "2":
            Peliculas_V2.borrar_peliculas()
            Peliculas_V2.esperarTecla() 
        case "3":
            Peliculas_V2.mostrarPeliculas()   
            Peliculas_V2.esperarTecla()
        case "4":
            Peliculas_V2.agreagarCaracteristicaPeliculas() 
            Peliculas_V2.esperarTecla()
        case "5": 
            Peliculas_V2.modificarCaracteristcaPeliculas()
            Peliculas_V2.esperarTecla()
        case "6": 
            Peliculas_V2.borrarCaracteristicaPeliculas()
            Peliculas_V2.esperarTecla()
        case "7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
            Peliculas_V2.esperarTecla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            opsion=True 
            input("Opción invalida vuelva a intentarlo ... por favor")