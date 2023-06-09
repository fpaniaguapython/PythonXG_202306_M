tupla1 = ()
tupla2 = tuple()
tupla3 = (3, 4, "Ramón")
tupla4 = ("Uno",)#Si sólo tiene un elemento, hay que poner una coma

print(tupla3[1])
#tupla3[1]="Cuatro" #Error, las tuplas son inmutables

lista3 = list(tupla3)
tupla5 = tuple(lista3)

#Lectura de fichero de datos, eliminación de \n y conversión a tupla
with open("palabras_prohibidas.txt", encoding="utf-8") as fichero:
    palabras = tuple([linea.replace('\n','') for linea in fichero.readlines()])

print(palabras)

