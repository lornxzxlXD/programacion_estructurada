from funciones import limpiar_pantalla, pausar
from usuarios.usuario import registrar_usuario, login_usuario, obtener_usuario_actual

def menu_inicio_sesion():
    while True:
        limpiar_pantalla()
        print("\t\t\t\t\t.:: Cocina Económica ::.")
        print("\t\t\t1.- 📝 Registro")
        print("\t\t\t2.- 🔐 Login")
        print("\t\t\t3.- 🚪 Salir")
        opcion = input("\n\t\tElige una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            if login_usuario():
                menu_usuario()
        elif opcion == "3":
            limpiar_pantalla()
            print("\n\t🎉 Gracias por usar el sistema de la tiendita. ¡Hasta pronto!\n")
            break
        else:
            print("\t\t\t❌ Opción inválida")
            pausar()

def menu_usuario():
    from ventas.ventas import registrar_venta
    usuario_actual = obtener_usuario_actual()
    while True:
        limpiar_pantalla()
        print(f"\t\t\t\t👤 Usuario: {usuario_actual['nombre']}")
        print("\t\t\t\t\t📋 MENÚ PRINCIPAL")
        print("\t\t\t\t1. ➕ Registrar Producto")
        print("\t\t\t\t2. 📦 Ver Productos")
        print("\t\t\t\t3. 🗑️ Borrar Producto")
        print("\t\t\t\t4. 💲 Actualizar Precio")
        print("\t\t\t\t5. 📥 Actualizar Stock")
        print("\t\t\t\t6. 🛒 Registrar Venta")
        print("\t\t\t\t7. 📈 Ver Ventas")
        print("\t\t\t\t8. 🚪 Cerrar Sesión")
        opcion = input("\n\t\tElige una opción: ")

        if opcion == "1":
            from productos.productos import registrar_producto
            registrar_producto()
        elif opcion == "2":
            from productos.productos import ver_inventario
            ver_inventario()
        elif opcion == "3":
            from productos.productos import eliminar_producto
            eliminar_producto()
        elif opcion == "4":
            from productos.productos import actualizar_precio
            actualizar_precio()
        elif opcion == "5":
            from productos.productos import actualizar_stock
            actualizar_stock()
        elif opcion == "6":
            registrar_venta(usuario_actual["id"])
        elif opcion == "7":
            from ventas.ventas import ver_ventas
            ver_ventas()
        elif opcion == "8":
            limpiar_pantalla()
            print("Cerrando sesión...")
            break
        else:
            print("\t\t\t❌ Opción inválida")
            pausar()

def main():
    menu_inicio_sesion()

if __name__ == "__main__":
    main()
