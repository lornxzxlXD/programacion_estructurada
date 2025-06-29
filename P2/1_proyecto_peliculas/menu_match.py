import os
os.system("cls")


def menu_de_opciones():
    opcion=int(input(f"\t\t..::Bienvenido al menu de peliculas::..\t\n seleccione una opcion (1-7): \n\t 1.- agregar pelicula \n\t 2.-borrar pelicula \n\t 3.-modificar\n\t 4.-consultar las peliculas \n\t 5.-buscar las peliculas \n\t 6.-vaciar las peliculas \n\t 7.-salir del menu \n"))
    
    match opcion:
        case 1:
            pelicula_agregada = input("¿Qué película desea agregar? ")
        case 2:
            delete_pelicula = input("¿Qué película desea borrar? ")
        case 3:
            pelicula_mod = input("¿Qué película desea modificar? ")
        case 4:
            cons_pelicula = input("¿Qué película desea consultar? ")
        case 5:
            buscar_pelicula = input("¿Qué película está buscando? ")
        case 6:
            vaciar_peliculas = input("Se vaciaron las películas. Pulsa cualquier tecla para continuar. ")
        case 7:
            print("Listo, el sistema se finalizó con éxito.")
        case _:
            print("Opción no válida, vuelva a intentar.")
            input("Pulsa cualquier tecla para continuar.")


menu_de_opciones()