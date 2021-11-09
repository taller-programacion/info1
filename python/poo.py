class Animal:

    #Atributos o Propiedades
                #('mamifero', 100,4 )
    def __init__(self, especie, edad, numPatas):
        self.especie = especie  #self.especie = mamifero
        self.edad = edad
        self.numPatas = numPatas

    #Métodos o acciones que realiza el Animal
    def sonido(self):
        print("DASDASFW32423%%&5DASD23E32D")
        #pass

    def caracteristicas(self):
        return type(self).__name__  #Lobo

    def moverse(self):
        pass

#Fin clase Animal

#Creando objetos a partir de Animal
#miAnimal = Animal('mamífero', 100, 4)
#print (miAnimal.especie)
#print (miAnimal.edad)
#print (miAnimal.numPatas)

class Lobo(Animal):
    def sonido(self):
        print("Grrrrr")

    def moverse(self):
        print("Caminando con 4 patas")

#Fin clase Lobo

class Ardilla(Animal):
    def sonido(self):
        print("Squir Smix")

    def moverse(self):
        print("Trepando árboles")
    
    def comer(self):
        print("Comiendo nueces")

#Fin clase

#Creando objetos

miLobo = Lobo('mamífero', 5, 4)
print ("\nMétodos\n")

#objeto.metodo()
print("Soy un Animal del tipo", miLobo.caracteristicas()) #Lobo
print (miLobo.caracteristicas())
print (miLobo.sonido())
print (miLobo.moverse())

print ("\nPropiedades\n")
print (miLobo.especie)
print (miLobo.edad)
print (miLobo.numPatas)

juanito = Ardilla('mamífero', 10, 4)
print ("\nMétodos\n")

#objeto.metodo()
print("Soy un Animal del tipo", juanito.caracteristicas())
print (juanito.sonido())
print (juanito.moverse())
print (juanito.comer())

print ("\nPropiedades\n")
print (miLobo.especie)
print (miLobo.edad)
print (miLobo.numPatas)
