#Proyecto 3
#crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menu de opciones 
#que permita agregar, mostrar y calcular promedios de las calificaciones de los alumnos

#Notas
#1.- utilizar fuciones y mandar llamar desde otro archivo
#2.- utilizar listas para almacenar el nombre del alumno y 3 calificaciones 


import calificaciones

def main():
    opcion = True
    datos = []

    while opcion:
        calificaciones.borra_pantalla()
        opcion = calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_alumno(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_alumnos(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_calificaciones(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscar_alumno(datos)
                calificaciones.esperarTecla()
            case "5":
                print("\n👋 Terminaste la ejecución del sistema. ¡Hasta luego!")
                calificaciones.esperarTecla()
                opcion = False
            case _:
                print("\n❌ Opción inválida. Vuelve a intentarlo, por favor.")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()
