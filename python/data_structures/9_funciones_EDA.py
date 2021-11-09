# -*- coding: utf-8 -*-
# ------------- Funciones con tuplas y diccionarios -------------

def recibirLista(lista):
    print ("Lista:", lista)

def recibirTupla(*tupla): #Operador * para esperar tupla
    print ("Tupla:", tupla)


def recibirDiccionario(**dico): #Operador ** para esperar diccionario
    print ("Diccionario:", dico)
    return dico

def recibirSubDiccionario(**dico): #Operador ** para esperar diccionario
    recibirDiccionario(**dico)

recibirLista(['hola', 'adios'])
recibirTupla(8, 9)
dicc = recibirDiccionario(Tipo=3, OO=True)
recibirDiccionario(Python=dicc, Java=8)
