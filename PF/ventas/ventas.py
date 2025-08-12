# ventas/ventas.py
from conexionBD import obtener_conexion
from funciones import limpiar_pantalla, pausar
from productos.productos import ver_inventario
from ticket.ticket import generar_ticket
def registrar_venta(id_vendedor):
    limpiar_pantalla()
    print("\n\t\t\t\t== 🛒 Registrar Venta ==")

    carrito = []
    total_general = 0

    try:
        conexion = obtener_conexion()
        if not conexion:
            print("\n\t\t\t❌ No se pudo conectar a la base de datos.")
            pausar()
            return
        cursor = conexion.cursor()

        while True:
            # Mostrar inventario una sola vez
            print("\n\t\t\t\t📦 Productos disponibles:\n")
            cursor.execute("SELECT id_producto, nombre, precio, stock FROM productos WHERE stock > 0")
            productos = cursor.fetchall()
            for p in productos:
                print(f"ID: {p[0]} | {p[1]} | 💲{p[2]} | Stock: {p[3]}")

            try:
                id_producto = int(input("\n\t\t\tID del producto: "))
                cantidad = int(input("\t\t\tCantidad: "))
            except ValueError:
                print("\n\t\t\t❌ Ingresa un número válido.")
                continue

            # Verificar existencia
            cursor.execute("SELECT nombre, precio, stock FROM productos WHERE id_producto = %s", (id_producto,))
            datos = cursor.fetchone()

            if not datos:
                print("\n\t\t\t❌ Producto no encontrado.")
                continue

            nombre, precio, stock = datos
            if cantidad > stock:
                print("\n\t\t\t❌ Stock insuficiente.")
                continue

            subtotal = precio * cantidad
            total_general += subtotal
            carrito.append((id_producto, nombre, cantidad, precio, subtotal))

            print(f"\n\t\t\t✅ {cantidad} x {nombre} agregado. Subtotal actual: 💲{total_general}")

            # Preguntar si quiere agregar más
            opcion = input("\n\t\t\t¿Quieres agregar otro producto? (s/n): ").strip().lower()
            if opcion != "s":
                break

        # Registrar todos los productos en la venta
        if carrito:
            for id_prod, nombre, cantidad, precio, subtotal in carrito:
                cursor.execute("""
                    INSERT INTO ventas (id_producto, id_usuario, cantidad, total)
                    VALUES (%s, %s, %s, %s)
                """, (id_prod, id_vendedor, cantidad, subtotal))

                cursor.execute("UPDATE productos SET stock = stock - %s WHERE id_producto = %s", (cantidad, id_prod))

            conexion.commit()
            generar_ticket(id_vendedor, carrito, total_general)
            print("\n\t\t\t✅ Venta registrada correctamente.")
            print("\t\t\tTotal a pagar: 💲", total_general)
        else:
            print("\n\t\t\t⚠️ No se registraron productos en la venta.")

        conexion.close()
    except Exception as e:
        print(f"\n\t\t\t❌ Error: {e}")

    pausar()



def ver_ventas():
    limpiar_pantalla()
    print("\n\t\t\t\t== 📈 Ventas ==")
    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT v.id_venta, p.nombre, u.username, v.cantidad, v.total
                FROM ventas v
                JOIN productos p ON v.id_producto = p.id_producto
                JOIN usuarios u ON v.id_usuario = u.id_usuario
            """)
            ventas = cursor.fetchall()
            for v in ventas:
                print(f"\n\t\t\tID Venta: {v[0]} | Producto: {v[1]} | Vendedor: {v[2]} | Cantidad: {v[3]} | Total: 💲{v[4]}")
            conexion.close()
    except Exception as e:
        print(f"\n\t\t\t❌ Error: {e}")
    pausar()
