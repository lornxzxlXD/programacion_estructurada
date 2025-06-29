#proyecto 1. crear un proyecto que permita gestionar (administrar peliculas); colocar un menu de opciones para agregar, borrar
#modificar, consultar, buscar y vaciar peliculas 
#Notas: 1.- utilizar funciones y mandar llamar desde otro archivo. 2.- Utilizar una lizta para almacenar los nombres de las peliculas 
import os
os.system("cls")

def menu_de_opciones ():
    opcion=int(input(f"\t\t..::Bienvenido al menu de peliculas::..\t\n seleccione una opcion (1-7): \n\t 1.- agregar pelicula \n\t 2.-borrar pelicula \n\t 3.-modificar\n\t 4.-consultar las peliculas \n\t 5.-buscar las peliculas \n\t 6.-vaciar las peliculas \n\t 7.-salir del menu"))
    if opcion==1: 
        pelicula_agregada=input("¿que pelicula desea agregar?")
    elif opcion==2:
        delete_pelicula=input("¿que pelicula desea borrar?")
    elif opcion==3:
        pelicula_mod=input("¿Que pelicula desea modificar?")
    elif opcion==4:
        cons_pelicula=input("¿Que pelicula desea cosultar?")
    elif opcion==5:
        buscar_pelicula=input("¿Que pelicula esta buscando?")
    elif opcion==6:
        vaciar_peliculas=input("se vaciaron las peliculas pulsa cualquier tecla para continuar")
    elif opcion==7:
        print("listo el sistema se finalizo con exito")
    else :
        print("opcion no valida vuelva a intentar")
        input("pulse cualquier tecala para continuar")
   







