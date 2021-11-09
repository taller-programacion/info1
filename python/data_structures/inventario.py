# -*- coding: utf-8 -*-

# ------------- Diccionario -------------
#Solo se ermite una llave nula
#Los valores son mutables pero las llaves NO
#No se encuentran ordenados por ser hashmap
elementos = {'Abarrotes': {
                            'Pan':{},
                            'Leche':{}
                        }
            }

print ("Productos__________________________\n")
elementos['Abarrotes']['Pan'][0]= {'nombre': 'Pan Blanco', 'precio': 25.00, 'cantidad': 1020}
elementos['Abarrotes']['Pan'][1]= {'nombre': 'Pan Integral', 'precio': 23.00, 'cantidad': 20}
elementos['Abarrotes']['Leche'][0]= {'nombre': 'Leche Entera', 'precio': 20.00, 'cantidad': 10}
elementos['Abarrotes']['Leche'][1]= {'nombre': 'Leche Deslactosada', 'precio': 32.00, 'cantidad': 1010}


i=0
#for i in elementos['Abarrotes']['Pan'][i]:
#    print (i, elementos['Abarrotes']['Pan'][i]['nombre'])
#print (elementos['Abarrotes']['Leche'])
print ("Leche\n")
for i in elementos['Abarrotes']['Leche']:
    print ("\tID: " + str(i) + "\n")
    print ("\tNombre: " + str(elementos['Abarrotes']['Leche'][i]['nombre']) + "\n")
    print ("\tPrecio: " + str(elementos['Abarrotes']['Leche'][i]['precio']) + "\n")
    print ("\tCantidad: " + str(elementos['Abarrotes']['Leche'][i]['cantidad']) + "\n")
    print ("-----------------------------------------\n")


print ("Pan\n")
for i in elementos['Abarrotes']['Pan']:
    print ("\tID: " + str(i) + "\n")
    print ("\tNombre: " + str(elementos['Abarrotes']['Pan'][i]['nombre']) + "\n")
    print ("\tPrecio: " + str(elementos['Abarrotes']['Pan'][i]['precio']) + "\n")
    print ("\tCantidad: " + str(elementos['Abarrotes']['Pan'][i]['cantidad']) + "\n")
    print ("-----------------------------------------\n")
# Envía un error al imprimir un elemento inexistente
# print elementos['oxigeno']

