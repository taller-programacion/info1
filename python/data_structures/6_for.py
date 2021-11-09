# -*- coding: utf-8 -*-

# Ciclo for
lista = [3, 4, 5, 6]
for var in lista:
    print (var)
print("------------------------")
# La función range ayuda a generar un rango de números
lista1 = []
lista2 = []
lista3 = []
lista4 = []

print("------------------------")
for elemento in range(5, 10): #limite abierto n-1
    lista1.append(elemento)
    print ("Agregando elemento :", elemento)
    print ("Lista1 completa dentro del for: ",lista1)
print ("Lista1 completa fuera del for: ",lista1)
print("------------------------")
for elemento in range(5): #0...n-1 (0 1 2 3 4)
    lista2.append(elemento)
    print ("Agregando elemento :", elemento)
    print ("Lista2 completa dentro del for: ",lista2)
print (lista2)
print("------------------------")
listaRange = range(5, 50, 5) #Inicio 5, termino 50-1, incremento de 5
for elemento in listaRange:
    lista2.append(elemento)    
    print ("Agregando elemento :", elemento)
    print ("Lista2 completa dentro del for: ",lista2)
print("------------------------")
for elemento in range(5):
    print ("Hola")
print("------------------------")
for elemento in "programando aqui":
    #elemento = p
    print (elemento.upper())

print("------------------------")
for i in range(5, 0, -1): #5 4 3 2 1
    lista3.append(i)
print (lista3)


print("------------------------")
for i in range(-6, 7, 2): #-6 -4 -2 0 2 4 6
    print(i)

print("------------------------")
#Range NO permite decimales
for i in range(0, 5): #0 0.1 -0.2 0.3 0.4 0.5 0.6
    print(i/10, end=' | ') #end cambia final de linea, por default es salto de linea
print("\n------------------------")

