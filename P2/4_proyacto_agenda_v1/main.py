#sistema de gestion de agenda de contactos

#crear una agenda que realice lo siguiente, agregar, mostrar todos los contratos ,buscar contacto por nombre, salir

import Agenda

Agenda.borrar_pantalla()
opcion = True



while opcion:
    print(f"\t\t\t\t..::: Sistema de Gestion de Agenda de Contactos:::.. \n\n\t\t\t\t\t1️⃣  Agregar contacto \n\t\t\t\t\t2️⃣  Mostrar todos los contactos \n\t\t\t\t\t3️⃣ buscar contactos por nombre \n\t\t\t\t\t4️⃣  salir")
    opcion=input(f"\n\t\t\t\t👉 Elige una opción (1-4): ").strip()


    match opcion:
        case "1":
            Agenda.agregar()
            Agenda.esperar_tecla()
            Agenda.borrar_pantalla()
        case "2":
            Agenda.mostrar()
            Agenda.esperar_tecla()
            Agenda.borrar_pantalla()
        case "3":
            Agenda.buscar()
            Agenda.esperar_tecla()
            Agenda.borrar_pantalla()
        case "4":
            opcion=False
            Agenda.esperar_tecla()
            Agenda.borrar_pantalla()
        case _:
            print(f"\n\t\t..:::el valor ingresado no es  correcto:::.. \n\t\t..:::porfavor intentelo otra vez:::...")
            input()
