# -*- coding: utf-8 -*-

# ------------- Listas -------------
# Declaracion de una lista simple
diasDelMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print (diasDelMes)
print ("Enero " + str(diasDelMes[0])) #31
print ("Julio " + str(diasDelMes[5])) #30
print ("Diciembre " + str(diasDelMes[11])) #31

# Declaracion de listas anidadas
numeros=[["cero", 0],['uno', 1, 'UNO'], ['dos', 2], ['tres', 3], ['cuatro', 4], [["cinco1", ["cinco2", 0]], 5]]
numeros1=[[["Hola", "Mundo"], 0],['uno', 1, 'UNO'], ['dos', 2], ['tres', 3], ['cuatro', 4], ['X', 5]]

#print (numeros)
#print (numeros[1][2])
#print (numeros[5][0][1][0])
#print (numeros1[0][0][1][5]) #Exception index

# Cambiando el valor de uno de los elementos de la lista
print (numeros1[5])
numeros1[5][0] = "cinco"
print (numeros1[5])
