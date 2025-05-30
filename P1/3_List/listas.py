
#Ejemplo 1 crear una lista de numeros e imprimir el contenido 
import os 
os.system('cls')

#1er froma
ListaNumeros=[23,45,8,24]
ListaNumeros.sort()
print(ListaNumeros)

#2da forma valor
for i in ListaNumeros:
    print(i)

#3ra forma indices
for i in range(0,len(ListaNumeros)):
    print(ListaNumeros[i])


input("pulsa cualquier tecla")
os.system('cls')
#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

palabras=["hola","casa","jupiter","sol"]

#1er forma
palabra_buscada=input("ingresa la palabra a buscar: ")

if palabra_buscada in palabras:
    print("se encontro la palabra")
else:
    print("no se encontro la palabra")

#2da forma
enconto=False
for i in palabras:
    if i==palabra_buscada:
       encontro=True

if encontro==True:
    print("se encontro la palabra")
else:
    print("no se encontro la palabra")

#3ra forma 
enconto=False
for i in range(len(palabras)):
   if palabras[i]==palabra_buscada:
       encontro=True

if encontro:
    print("se encontro la palabra")
else:
    print("no se encontro la palabra")



#ejemplo 3 añadir elementos a la lista
input("pulsa cualquier tecla")
os.system('cls')
numeros=[]
opc="si"

while opc=="si":
    numeros.append(float(input("Dame un numero entero o decimal ")))
    opc=input("¿Deseas solicitar otro numero? (si/no)").lower()

print(numeros)
 


 
#Ejemplo 4 Crear una lista multidimensional (matriz) que almacene el nimbre y telefono de 4 personas

agenda=[
    ["carlos","618 645 8585"],
    ["juan","618 474 9656"],
    ["diego","618 123 5556"],
    ["eduardo","618 947 6585"]
]

print(agenda)

for i in agenda:
    print(i)

valores=""
for r in range (0,3):
    for c in range(0,2):
        valores+=f"{agenda[r][c]},"
    valores+=f"\n"
print(valores)
