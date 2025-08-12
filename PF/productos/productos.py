# productos/productos.py
from conexionBD import obtener_conexion
from funciones import limpiar_pantalla, pausar

def registrar_producto():
    limpiar_pantalla()
    print("\n\t\t\t\t== ➕ Registrar Producto ==")
    nombre = input("\t\t\tNombre del producto: ")
    precio = float(input("\t\t\tPrecio: "))
    stock = int(input("\t\t\tStock inicial: "))

    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)", (nombre, precio, stock))
            conexion.commit()
            conexion.close()
            print("\n\t\t\t✅ Producto registrado correctamente.")
    except Exception as e:
        print(f"\n\t\t\t❌ Error: {e}")
    pausar()

def ver_inventario():
    limpiar_pantalla()
    print("\n\t\t\t\t== 📦 Inventario ==")
    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_producto, nombre, precio, stock FROM productos")
            productos = cursor.fetchall()
            conexion.close()
            for p in productos:
                print(f"ID: {p[0]} | {p[1]} | 💲{p[2]} | Stock: {p[3]}")
    except Exception as e:
        print(f"\n\t\t\t❌ Error: {e}")
    pausar()

def eliminar_producto():
    ver_inventario()
    id_producto = int(input("\t\t\tID del producto a eliminar: "))
    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
            conexion.commit()
            conexion.close()
            print("\n\t\t\t✅ Producto eliminado.")
    except Exception as e:
        print(f"\n\t\t\t❌ Error: {e}")
    pausar()

def actualizar_precio():
    ver_inventario()
    id_producto = int(input("\t\t\tID del producto: "))
    nuevo_precio = float(input("\t\t\tNuevo precio: "))
    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("UPDATE productos SET precio = %s WHERE id_producto = %s", (nuevo_precio, id_producto))
            conexion.commit()
            conexion.close()
            print("\n\t\t\t✅ Precio actualizado.")
    except Exception as e:
        print(f"\n\t\t\t❌ Error: {e}")
    pausar()

def actualizar_stock():
    ver_inventario()
    id_producto = int(input("\t\t\tID del producto: "))
    nuevo_stock = int(input("\t\t\tNuevo stock: "))
    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("UPDATE productos SET stock = %s WHERE id_producto = %s", (nuevo_stock, id_producto))
            conexion.commit()
            conexion.close()
            print("\n\t\t\t✅ Stock actualizado.")
    except Exception as e:
        print(f"\n\t\t\t❌ Error: {e}")
    pausar()
