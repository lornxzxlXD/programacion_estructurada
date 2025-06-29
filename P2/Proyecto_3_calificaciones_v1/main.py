#Proyecto 3
#crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menu de opciones 
#que permita agregar, mostrar y calcular promedios de las calificaciones de los alumnos

#Notas
#1.- utilizar fuciones y mandar llamar desde otro archivo
#2.- utilizar listas para almacenar el nombre del alumno y 3 calificaciones 

import calificaciones

def main():
    opcion=True
    datos=[]
    while opcion:
        calificaciones.borra_pantalla()
        opcion=calificaciones.menu_principal()
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
                opcion=False    
                print("Terminaste la ejecucion del SW")
                calificaciones.esperarTecla()
                print("\n\tTerminaste la ejecucion del SW")
            case _:
                opcion=True 
                input("Opción invalida vuelva a intentarlo ... por favor")

if __name__=="__main__":
    main()

    