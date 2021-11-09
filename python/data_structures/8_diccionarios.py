# -*- coding: utf-8 -*-

# ------------- Diccionario -------------
#Solo se ermite una llave nula
#Los valores son mutables pero las llaves NO
#No se encuentran ordenados por ser hashmap
elementos = {'hidrogeno': 1, 'helio': 2, 'carbon': 6}

# Al imprimir el diccionario, los elementos puede
# aparecer en diferente orden del introducido
print (elementos)
print (elementos['hidrogeno'])

# Envía un error al imprimir un elemento inexistente
# print elementos['oxigeno']

# Se pueen agregar elementos al diccionario
elementos['litio'] = 3
elementos['nitrogeno'] = 8
elementos['hidrogeno'] = 1000 #Si existe lo actualiza, en caso contrario lo agrega
print (elementos)

# Se crea un nuevo diccionario
elementos2 = {}
elementos2['H'] = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}
elementos2['He'] = {'name': 'Helium', 'number': 2, 'weight': 4.002602}

print (elementos2)

# Se imprimen los datos de un elemento del diccionario
print (elementos2['H'])
print (elementos2['H']['name'])
print (elementos2['H']['number'])
# Se cambia el valor de un elemento
elementos2['H']['weight'] = 4.30
print (elementos2['H']['weight'])

# Se agregan elementos a una llave
elementos2['H'].update({'gas noble': True})
print (elementos2['H'])

# Muestra todas las llaves del diccionario
print (elementos2.keys()) #Devuelve listas
# Muestra todos los valores del diccionario
print (elementos2.items()) #Devuelve listas con subtuplas

for k,v in elementos2.items(): #Iterar y leer tuplas
    print ("Llave: " + str(k))
    print ("Valor: " + str(v))
    for subk, subv in v.items():
        print ("\tSUBLlave: " + str(subk))
        print ("\tSUBValor: " + str(subv))



# Se limpia el diccionario
#elementos2.clear()
print('\n')
elementos2['H'].clear()
print (elementos2)
print('\n')
elementos2['He'].clear()
print (elementos2)

# Eliminar con operacion del, elimina elemento por medio de llave
del(elementos2['He'])
print (elementos2)
