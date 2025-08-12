from conexionBD import obtener_conexion

def generar_ticket(id_venta):
    try:
        conexion = obtener_conexion()
        if not conexion:
            print("\n\t\t\t❌ No se pudo conectar a la base de datos para generar el ticket.")
            return
        cursor = conexion.cursor()
        cursor.execute("SELECT u.username, v.fecha_venta, v.total FROM ventas v JOIN usuarios u ON v.id_usuario = u.id_usuario WHERE v.id_venta = %s", (id_venta,))
        venta = cursor.fetchone()

        if not venta:
            print("\n\t\t\tVenta no encontrada.")
            conexion.close()
            return

        usuario_nombre, fecha_venta, total = venta

        print("\n\t\t\t\t===== TICKET DE VENTA =====")
        print(f"\t\t\tVenta No.: {id_venta}")
        print(f"\t\t\tVendedor: {usuario_nombre}")
        print(f"\t\t\tFecha: {fecha_venta}")
        print("\t\t\tProductos:")

        cursor.execute("SELECT p.nombre, t.cantidad, t.precio_unitario, t.subtotal FROM ticket t JOIN productos p ON t.id_producto = p.id_producto WHERE t.id_venta = %s", (id_venta,))
        items = cursor.fetchall()

        for item in items:
            print(f"{item[0]} | Cantidad: {item[1]} | Precio: ${item[2]:.2f} | Subtotal: ${item[3]:.2f}")

        print(f"TOTAL: ${total:.2f}")
        print("============================")
        conexion.close()
    except Exception as e:
        print(f"\n\t❌ Error al generar ticket: {e}")