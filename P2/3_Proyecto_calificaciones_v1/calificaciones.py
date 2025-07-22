# calificaciones.py

def borra_pantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t🔘 Oprime una tecla para continuar...")

def menu_principal():
    print("\n\t📚 ..::: SISTEMA DE CALIFICACIONES :::..\n")
    print(" 1️⃣  Agregar alumno")
    print(" 2️⃣  Mostrar alumnos")
    print(" 3️⃣  Calcular promedios")
    print(" 4️⃣  Buscar alumno 🔍")
    print(" 5️⃣  Salir 🚪")
    opcion = input("\n\t👉 Elige una opción (1-5): ").strip()
    return opcion


def agregar_alumno(alumnos):
    borra_pantalla()
    print("\n\t➕ .:: Registro de Alumno ::.\n")
    nombre = input("👤 Nombre del alumno: ").strip().upper()
    matricula = input("🆔 Matrícula del alumno: ").strip().upper()
    cuatrimestre = input("📅 Cuatrimestre: ").strip().upper()

    try:
        p1 = float(input("📝 Calificación P1: "))
        p2 = float(input("📝 Calificación P2: "))
        p3 = float(input("📝 Calificación P3: "))
        proyecto = float(input("📊 Calificación Proyecto: "))
    except ValueError:
        print("\n❌ Entrada inválida. Las calificaciones deben ser números.")
        return

    alumno = [nombre, matricula, cuatrimestre, p1, p2, p3, proyecto]
    alumnos.append(alumno)
    print("\n✅ Alumno registrado exitosamente.\n")

def mostrar_alumnos(alumnos):
    borra_pantalla()
    print("\n\t📋 .:: Listado de Alumnos ::.\n")
    if not alumnos:
        print("⚠️ No hay alumnos registrados.")
    else:
        for i, alumno in enumerate(alumnos, 1):
            print(f"{i}. 👤 {alumno[0]} | 🆔 Matrícula: {alumno[1]} | 📅 Cuatrimestre: {alumno[2]}")
            print(f"   📘 P1: {alumno[3]}, 📗 P2: {alumno[4]}, 📕 P3: {alumno[5]}, 📊 Proyecto: {alumno[6]}")

def calcular_calificaciones(alumnos):
    borra_pantalla()
    print("\n\t📈 .:: Promedios de Calificaciones ::.\n")
    if not alumnos:
        print("⚠️ No hay alumnos registrados.")
    else:
        for i, alumno in enumerate(alumnos, 1):
            promedio = (alumno[3] + alumno[4] + alumno[5] + alumno[6]) / 4
            print(f"{i}. 👤 {alumno[0]} | 🧮 Promedio: {promedio:.2f}")

def buscar_alumno(alumnos):
    borra_pantalla()
    print("\n\t🔍 .:: Buscar Alumno por Nombre ::.\n")

    nombre_buscar = input("🧑 Ingresa el nombre del alumno a buscar: ").strip().upper()
    encontrados = [a for a in alumnos if a[0] == nombre_buscar]

    if encontrados:
        print(f"\n✅ Se encontraron {len(encontrados)} alumno(s) con el nombre '{nombre_buscar}':\n")
        print("-------------------------------------------------------------------------------")
        print(" NOMBRE           | MATRÍCULA     | P1  | P2  | P3  | PROYECTO | CUATRIMESTRE")
        print("-------------------------------------------------------------------------------")
        for alumno in encontrados:
            print(f" {alumno[0]:<16} | {alumno[1]:<13} | {alumno[3]:<3} | {alumno[4]:<3} | {alumno[5]:<3} | {alumno[6]:<8} | {alumno[2]}")
        print("-------------------------------------------------------------------------------")
    else:
        print(f"\n❌ No se encontró ningún alumno con el nombre '{nombre_buscar}'.")
