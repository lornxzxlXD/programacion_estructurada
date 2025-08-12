from conexionBD import obtener_conexion
from funciones import limpiar_pantalla, pausar
import hashlib
import getpass

usuario_actual = None  # Guardar sesión

def registrar_usuario():
    limpiar_pantalla()
    print("\n\t\t\t\t== 📝 Registro de Usuario ==")
    nombre = input("\t\t\tNombre: ")
    apellido = input("\t\t\tApellido: ")
    email = input("\t\t\tCorreo electrónico: ")
    password = getpass.getpass("\n\t\t\tContraseña: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO usuarios (username, email, password)
                VALUES (%s, %s, %s)
            """, (f"{nombre} {apellido}", email, password_hash))
            conexion.commit()
            conexion.close()
            print("\n\t\t\t✅ Usuario registrado exitosamente.")
        else:
            print("\n\t\t\t❌ No se pudo conectar a la base de datos.")
    except Exception as e:
        print(f"\n\t\t\t❌ Error: {e}")
    pausar()

def login_usuario():
    global usuario_actual
    limpiar_pantalla()
    print("\n\t\t\t\t== 🔐 Iniciar Sesión ==")
    email = input("\t\t\tCorreo electrónico: ")
    password = getpass.getpass("\t\t\tContraseña: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_usuario, username FROM usuarios WHERE email = %s AND password = %s", (email, password_hash))
            usuario = cursor.fetchone()
            conexion.close()
            if usuario:
                usuario_actual = {"id": usuario[0], "nombre": usuario[1]}
                print(f"\n\t\t\t✅ Bienvenido, {usuario[1]}!")
                pausar()
                return True
            else:
                print("\n\t\t\t❌ Credenciales incorrectas")
        else:
            print("\n\t\t\t❌ Error de conexión.")
    except Exception as e:
        print(f"\n\t\t\t❌ Error: {e}")
    pausar()
    return False

def obtener_usuario_actual():
    global usuario_actual
    return usuario_actual
