from conexionBD import *
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre,apellidos,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
        sql="insert into usuarios(nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s,)"
        val=(nombre,apellidos,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return None
    
def inicio_sesion(email,contrasena):
    try:
        sql = "SELECT * FROM usuarios WHERE email=%s AND password=%s"
        val=(email,contrasena)
        cursor.execute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None
    