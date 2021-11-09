# -*- coding: utf-8 -*-
# ------------- Funciones en listas -------------
#Pop en listas
print ("Lista A")
listaA = [1, 2, 3, 4]
print (listaA)
elem_borrado = listaA.pop(1)
print ("Eliminaste el elemento:", elem_borrado)
#listaA.pop(0) #Elimina primer elemento
print ("POP", listaA.pop(0))
print (listaA)

#La función del sirve para eliminar elementos de una lista
print ("Lista B")
listaB = [3, 4, 5, 6]
print (listaB)
del(listaB[3])
print ("DEL [2]")
print (listaB)

#Insertando elementos en la lista
print ("INSERT 5")
listaB.insert(3, 15)
print ("INSERT 15")
listaB.insert(4, 1)
print (listaB)
listaB.insert(0, 10)
print (listaB)
