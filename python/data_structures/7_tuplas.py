# -*- coding: utf-8 -*-

# ------------- Tuplas -------------
# Declaración de una tupla
diasDelMes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#diasDelMes = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 #Otra forma de declarar una tupla

print (diasDelMes)
print ("Enero: " + str(diasDelMes[0]))
print ("Junio: " + str(diasDelMes[5]))
print ("Diciembre: " + str(diasDelMes[11]))

# Declaración de tuplas anidadas
numeros = (('cero', 0), ('uno', 1, 'UNO'), ('dos', 2),
        ('tres', 3), ('cuatro', 4), ('X', 5))

print (numeros)        # imprime tupla completa

#No se puede cambiar el valor de los elementos de la tupla
#numeros[5][0] = "cinco"

print (numeros[0]) 
print (numeros[2][0]) 
print (numeros[1][2])
