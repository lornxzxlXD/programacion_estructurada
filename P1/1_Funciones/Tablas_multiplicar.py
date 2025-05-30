"""
crear un programa que calcule e imprima la tabla de multiplicar del 2

Restriccciones:
1.- sin estructuras de control
2.- sin funciones
"""
import os
os.system('cls')
#version1
Uno=1*2
dos=2*2
tres=3*2
cuatro=4*2
cinco=5*2
seis=6*2
siete=7*2
ocho=8*2
nueve=9*2
diez=10*2

print(f"2x1={Uno}")
print(f"2x2={dos}")
print(f"2x3={tres}")
print(f"2x4={cuatro}")
print(f"2x5={cinco}")
print(f"2x6={seis}")
print(f"2x7={siete}")
print(f"2x8={ocho}")
print(f"2x9={nueve}")
print(f"2x10={diez}")

input("oprima cualquier tecla ")
import os
os.system('cls')

#version 2

tabla=int(input("ingrese el numero del que quieres imprimir la tabla"))

Uno=1*tabla
dos=2*tabla
tres=3*tabla
cuatro=4*tabla
cinco=5*tabla
seis=6*tabla
siete=7*tabla
ocho=8*tabla
nueve=9*tabla
diez=10*tabla

print(f"{tabla}x1={Uno}")
print(f"{tabla}x2={dos}")
print(f"{tabla}x3={tres}")
print(f"{tabla}x4={cuatro}")
print(f"{tabla}x5={cinco}")
print(f"{tabla}x6={seis}")
print(f"{tabla}x7={siete}")
print(f"{tabla}x8={ocho}")
print(f"{tabla}x9={nueve}")
print(f"{tabla}x10={diez}")

input("oprima cualquier boton para continuar")

import os 
os.system('cls')

#version 3
tabla=int(input("ingrese un numero paara imprimir tabla de multiplicar"))
for i in range(1,11):
    multiplicacion=i*tabla
    print(f"{i}x{tabla}={multiplicacion}")

#version 4 
os.system("cls")
def TablaMultiplicar():
    for i in range(1,11):
        multiplicacion=i*tabla
        print(f"{i}x{tabla}={multiplicacion}")

TablaMultiplicar()
