fichero_series = open("datos.txt", mode="r", encoding="utf-8")#r es el modo de apertura de lectura de ficheros de texto

#datos = fichero_series.read()#Lee todo el contenido del fichero

#datos = fichero_series.read(10)#Lee los 10 primeros caracteres
#datos = fichero_series.read(5)#Lee los 5 siguientes a la lectura anterior

#datos = fichero_series.readline()#Lee una línea y el salto de línea final
#datos = datos.replace('\n','')#Para eliminar los saltos de línea

datos = fichero_series.readlines()#Devuelve una lista con todas las líneas
datos = [linea.replace('\n','') for linea in datos]#Eliminamos los \n de las líneas de la lista obtenida

fichero_series.close()

print(datos)

#Estructura with, no es necesario cerrar los ficheros
with open("datos.txt", mode="r", encoding="utf-8") as fichero_series:
    datos = fichero_series.read()
    print(fichero_series.closed)#False, porque no está cerrado
print(fichero_series.closed)#True, porque al salir del bloque with, se autocierra
