"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funciones que no recibe parametros y no regresa valor
def solicitarDatos1():
    nombre=input("nombre: ")
    telefono=input("telefono: ")
    print(f"nombre: {nombre} y su telefono: {telefono}")
    
#3.- Funciones que recibe parametros y no regresa valor
def solicitarDatos3(nom,tel):
    nombre=nom
    telefono=tel
    print(f"nombre: {nombre} y su telefono: {telefono}")
    
#2.- Funciones que no recibe parammetros y regresa valor
def solicitarDatos2():
    nombre=input("nombre: ")
    telefono=input("telefono: ")
    return nombre,telefono

#4.- Funciones que recibe parametros y regresa valor 
def solicitarDatos4(nom,tel):
    nombre=nom
    telefono=tel
    return nombre,telefono



#Invocar las funciones 

solicitarDatos1()

nombre=input("Escribe el nombre: ")
telefono=input("Escrbe el telefono: ")

solicitarDatos3(nombre,telefono)

nom,tel=solicitarDatos2()
print(f"\t\n Los datod de la agenda son: \t\n Nombre: {nom}\t\n Telefono: {tel}") 


nom,tel=solicitarDatos4(nombre,telefono)
print(f"\t\n Los datod de la agenda son: \t\n Nombre: {nom}\t\n Telefono: {tel}") 
