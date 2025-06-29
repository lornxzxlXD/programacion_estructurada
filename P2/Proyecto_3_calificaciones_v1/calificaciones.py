#dict u objeto para al,acenar los atrivutos( nombre, categoria, clasificacion, genero, idioma)

#alunmo=¨[
#      "nombre alunmo",
#      "caificaciones del alumno (p1,p2,p3, proyecto final)":"",
#     "matricula del alumno":"",
#        "cuatrimestre en curso":"",
#        "calificacion final":""
#          ]



campos = ["Nombre", "Matrícula", "Cuatrimestre", "P1", "P2", "P3", "Proyecto"]

alumnos = []


def borra_pantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")
    
def menu_principal():
    print("\n\t..:::sistema de calificaciones:::... \n..::: sistema de gestion de califcaciones :::...\n\n 1.- agregar \n 2.- Mostrar  \n 3.- calcular promedios \n 4.- SALIR ")
    opcion=input("\t Elige una opción(1-4): ").upper()
    return opcion

def agregar_alumno(alumnos):
    nombre = input("Nombre del alumno: ").strip().upper()
    matricula = input("Matrícula del alumno: ").strip().upper()
    cuatrimestre = input("Cuatrimestre: ").strip().upper()
    p1 = float(input("Calificación P1: "))
    p2 = float(input("Calificación P2: "))
    p3 = float(input("Calificación P3: "))
    proyecto = float(input("Calificación Proyecto: "))

    alumnos = [nombre, matricula, cuatrimestre, p1, p2, p3, proyecto]
    alumnos.append(alumnos)
    print("\nAlumno registrado exitosamente.\n")
    
    return alumnos

def mostrar_alumnos(alumnos):
    print("\nListado de alumnos:\n")
    for i, alumnos in enumerate(alumnos, 1):
        print(f"{i}. {alumnos[0]} | Matrícula: {alumnos[1]} | Cuatrimestre: {alumnos[2]}")
        print(f"   P1: {alumnos[3]}, P2: {alumnos[4]}, P3: {alumnos[5]}, Proyecto: {alumnos[6]}")
