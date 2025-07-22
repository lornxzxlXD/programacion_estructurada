#proyecto 1. crear un proyecto que permita gestionar (administrar peliculas); colocar un menu de opciones para agregar, borrar
#modificar, consultar, buscar y vaciar peliculas 
#Notas: 1.- utilizar funciones y mandar llamar desde otro archivo. 2.- Utilizar una lizta para almacenar los nombres de las peliculas 
import os
os.system("cls")

import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t...::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperaTecla ()
        case "2":
            peliculas.eliminarPeliculas()
            peliculas.esperaTecla () 
        case "3":
            peliculas.actualizarPeliculas() 
            peliculas.esperaTecla()     
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperaTecla()
        case "5": 
            peliculas.buscarPeliculas()
            peliculas.esperaTecla()
        case "6": 
            peliculas.vaciarPelicula()
            peliculas.esperaTecla()
        case "7":
            opcion=False    
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")


