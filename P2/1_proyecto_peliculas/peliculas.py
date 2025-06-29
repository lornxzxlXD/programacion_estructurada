peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def esperaTecla ():
    print("Oprima cualquier tecla para continuar ...")
    input()

def agregarPeliculas ():
    borrarPantalla()
    print("\n\t.::agregar peliculas::. ")
    peliculas.append(input("ingresa el nombre: ").upper().strip())
    input("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO!:::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t.::Consultar Peliculas::. ")
    if len(peliculas)>0:
        for i in range (0,len(peliculas)):
            print(f"\t{i+1}: {peliculas[i]}")
    else:
        print("\n\t.::No hay peliculas en el Sistema en este momento... verificar")

def vaciarPelicula():
    borrarPantalla()
    print("\n\t.::Vaciar o quitar TODAS las películas::.")  
    resp = input("¿Deseas borrar TODAS las películas del sistema? (si/no): ").lower().strip()
    if resp == "si":
        peliculas.clear()
        input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    else:
        input("\n\t\t::: Operación cancelada :::")

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t.::Eliminar Pelicula::.")
    if len(peliculas)>0:
        for i in range (0,len(peliculas)):
            print(f"\t{i+1}: {peliculas[i]}")
    else:
        print("\n\t.::No hay peliculas en el Sistema en este momento... verificar")
    print("¿Que Pelicula Desea Eliminar o Borrar? (Porfavor Ingrese El Numero De La Pelicula Que Desea Eliminar)")
    i=int(input())
    peliculas.pop(i-1)
    input("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO!:::")



