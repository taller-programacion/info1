# -*- coding: utf-8 -*-

# ------------- Funciones en listas -------------
lista = ['H', 'o', 'l', 'a']
lista2 = ['A', 'd', 'i', 'o', 's']

lista.append('s')           # Agrega un nuevo elemento a la lista

print (lista)
print (len(lista))          # Obtiene la longitud de la lista

lista3 = lista + lista2     # Concatena dos listas
print (lista3)
print (lista)
print (lista2)

lista_alfa = [0, 1, 2, [3, 4]]

print (len(lista_alfa))       # Solo imprime el numero de elementos externos
print (len(lista_alfa[3]))    # Imprime la longitud de la lista interna
#print (len(lista_alfa[0]))    # Imprime la longitud de la lista interna
