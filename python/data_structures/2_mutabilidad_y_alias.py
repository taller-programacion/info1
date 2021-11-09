# -*- coding: utf-8 -*-

# ------------- Mutacion y referencias -------------

c1 = 'Hola'
c2 = c1        # Otra referencia a la cadena

print (c1)
print (c2)

#print (c2[3])

#c1[0] = 'B'    # operacion no permitida
#c1[0] = c2    # operacion no permitida
c1 = 'Bola'    # Nueva cadena creada

# Al imprimir las cadenas, ya no son iguales, no apuntan a la misma información
print (c1)
print (c2)

# ------------- Listas -------------
lista = ['H', 'o', 'l', 'a']
lista2 = lista     # Otra referencia a la lista
print("Listas originales")
print("Lista 1")
print (lista)
print("Lista 2")
print (lista2)

print("Cambio lista original")
lista[0] = 'B'
print("Lista 2")
#lista2[0] = 'Y'
lista2[1] = 'g' 
lista2[1] = 'V' 
# Al imprimir las listas, las dos referencias apuntan a la misma informacion
print("Imprimo las dos listas")
print (lista)
print (lista2)


def mutarLista(lista):
    lista[3] = 'G'
    
def mutarLista2(lista):
    lista[0]= 'H'



mutarLista(lista)
print("Mutar desde función")
print (lista)

mutarLista2(lista2)
print("Mutar segunda lista")
print (lista)
