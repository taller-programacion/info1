# -*- coding: utf-8 -*-

# ------------- Funciones en listas -------------
lista_alfa = [0, 1, 10, 15, [3, 4, 10, 20, 5]]
# Uso de index en listas
print (lista_alfa.index(15))
print (lista_alfa[4].index(20))
#print (lista_alfa[3].index(1)) #Error por indice

if 15 in lista_alfa:
    print ("Find")
else:
    print ("Not Find")

# Uso de in en listas
print ("IN")
print (2 in lista_alfa)
print (1 in lista_alfa)
print (100 in lista_alfa[4])

print ("NOT IN")
#Uso de not in en listas
print (2 not in lista_alfa)
print (3 not in lista_alfa)
print (3 not in lista_alfa[4])
print (not 100 in lista_alfa[4])
