#dict u objeto para al,acenar los atrivutos( nombre, categoria, clasificacion, genero, idioma)

# 🎬 Película con datos detallados
pelicula = {}

def borra_pantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t🔘 Oprime una tecla para continuar...")

def crear_peliculas():
    borra_pantalla()
    print("\n\t🎬 .:: Alta de Películas ::.\n")
    pelicula.update({"nombre": input("🎞️ Ingrese el nombre: ").upper().strip()})
    pelicula.update({"categoria": input("🏷️ Ingrese la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("🔒 Ingrese la clasificación: ").upper().strip()})
    pelicula.update({"genero": input("🎭 Ingrese el género: ").upper().strip()})
    pelicula.update({"idioma": input("🗣️ Ingrese el idioma: ").upper().strip()})
    print("\n\t✅ .:: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::.")

def mostrarPeliculas():
    borra_pantalla()
    print("\n\t📋 .:: Consultar la Película ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t📌 {i.capitalize()}: {pelicula[i]}")
    else:
        print("\t⚠️ .:: No hay películas en el sistema ::.")

def borrar_peliculas():
    borra_pantalla()
    print("\n\t🧹 .:: Borrar TODAS las Películas ::.\n")
    resp = input("❓ ¿Deseas borrar todas las películas del sistema? (si/no): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        print("\n\t✅ .:: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::.")
    else:
        print("\n\t⏹️ .:: Operación cancelada ::.")

def agreagarCaracteristicaPeliculas():
    borra_pantalla()
    print("\n\t➕ .:: Agregar Característica a la Película ::.\n")
    atributo = input("📝 Ingrese la nueva característica: ").lower().strip()
    valor = input(f"✏️ Ingrese el valor para '{atributo}': ").upper().strip()
    pelicula[atributo] = valor
    print("\n\t✅ .:: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::.\n") 

def modificarCaracteristcaPeliculas():
    borra_pantalla()
    print("\n\t🛠️ .:: Modificar Característica de la Película ::.\n")
    atributo = input("🔎 Ingrese la característica a modificar: ").lower().strip()
    if atributo in pelicula:
        nuevo_valor = input(f"✏️ Nuevo valor para '{atributo}': ").upper().strip()
        pelicula[atributo] = nuevo_valor
        print(f"\n\t✅ .:: ¡'{atributo}' se ha modificado con éxito! ::.\n")
    else:
        print(f"\n\t❌ .:: ¡'{atributo}' no existe en la película! ::.\n")

def borrarCaracteristicaPeliculas():
    borra_pantalla()
    print("\n\t🗑️ .:: Borrar Característica de la Película ::.\n")
    atributo = input("🔎 Ingrese la característica a borrar: ").lower().strip()
    if atributo in pelicula:
        del pelicula[atributo]
        print(f"\n\t✅ .:: ¡'{atributo}' se ha borrado con éxito! ::.\n")
    else:
        print(f"\n\t❌ .:: ¡'{atributo}' no existe en la película! ::.\n")
