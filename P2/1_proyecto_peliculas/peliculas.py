peliculas = []

def borrarPantalla():
    import os
    os.system("cls")

def esperaTecla():
    print("🔘 Oprima cualquier tecla para continuar ...")
    input()

def agregarPeliculas():
    borrarPantalla()
    print("\n\t🎞️ .:: Agregar Películas ::.")
    peliculas.append(input("🎬 Ingresa el nombre: ").upper().strip())
    input("\n\t✅ ::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t📋 .:: Consultar Películas ::.")
    if len(peliculas) > 0:
        for i in range(len(peliculas)):
            print(f"\t🎟️ {i+1}: {peliculas[i]}")
    else:
        print("\n\t⚠️ .:: No hay películas en el sistema en este momento... verificar ::.")

def vaciarPelicula():
    borrarPantalla()
    print("\n\t🧹 .:: Vaciar o quitar TODAS las películas ::.")  
    resp = input("❓ ¿Deseas borrar TODAS las películas del sistema? (si/no): ").lower().strip()
    if resp == "si":
        peliculas.clear()
        input("\n\t✅ ::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    else:
        input("\n\t⏹️ ::: Operación cancelada :::")

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t❌ .:: Eliminar Película ::.")
    if len(peliculas) > 0:
        for i in range(len(peliculas)):
            print(f"\t🗂️ {i+1}: {peliculas[i]}")
        print("🗑️ ¿Qué película deseas eliminar? (ingresa el número correspondiente)")
        try:
            i = int(input("👉 Número: "))
            if 1 <= i <= len(peliculas):
                peliculas.pop(i - 1)
                input("\n\t✅ ::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
            else:
                input("\n\t⚠️ Número fuera de rango.")
        except ValueError:
            input("\n\t❌ Entrada inválida. Solo se aceptan números.")
    else:
        print("\n\t⚠️ .:: No hay películas en el sistema en este momento... verificar ::.")
