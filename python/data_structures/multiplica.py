# -*- coding: utf-8 -*-

# ------------- Listas -------------

# Declaracion de listas anidadas
n=[[1,2,3,4,5,6,7,8,9,10],
   [2,4,6,8,10,12,14,16,18,20],
   [3,6,9,12,15,18,21,24,27,30],
   [4,8,12,16,20,24,28,32,36,40]
   ]


tablaV2 = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        ]

tablaV3 = [0]*10 #Crea una lista con 10 elementos

l=c=1

#While tablaV3
while l <=10:
    tablaV3[l-1] = [0]*10
    while c <=10:
        tablaV3[l-1][c-1] = l * c
        c +=1
    c = 1
    l += 1



#While tablaV2
while l <=10:
    while c<=10:
        tablaV2[l-1][c-1] = l * c
        c += 1
    c=1
    l+=1


# Cambiando el valor de uno de los elementos de la lista
#numeros[1][2] = "dos"

def multiplicar(entReg, entCol):
   #return n[entReg - 1][entCol -1]
   #return tablaV2[entReg - 1][entCol -1]
    return tablaV3[entReg - 1][entCol -1]


def main():
    print ("\tTablas de multiplicar")
    print ("2 * 2 =", multiplicar(2,2), "\n")
    print ("9 * 9 =", multiplicar(9,9), "\n")

if __name__ == '__main__':
    main()
