
inventario = {} #Crear Inventario

def actualizar(cadProducto, cadLlave, entValor): #Agregar Elementos
    inventario[cadProducto][cadLlave] = entValor


def main():
    inventario['refresco'] = {'precio': '$15', 'cantidad': '100'}
    inventario['papas'] = {'precio': '$10', 'cantidad': '30'}
    inventario['leche'] = {'precio': '$29', 'cantidad': '130'}

    print("El inventario actual es:\n")
    
    for i in inventario:
        print (i, inventario[i])

    r = "refresco"
    p = "precio"
    precior = "16"
    c = "cantidad"
    l = "leche"
    cantidadl = "39"

    actualizar(r, p, precior)
    actualizar(l, p, cantidadl)

    print("El inventario despúes de las modificaciones es:\n")

    for i in inventario:
        print (i, inventario[i])
        
if __name__ == '__main__':
    main()


