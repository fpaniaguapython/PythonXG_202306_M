contador = 0
while contador<10:
    contador+=1
print(contador)

contador=0
while contador<10:
    contador+=1
    if contador==5:
        break #Suspender el bucle y salir fuera
print(contador)

#while con else
contador=0
while contador<10:
    contador+=1
    if contador==5:
        break #Suspender el bucle y salir fuera
else:#Sólo si la condición del while se deja de cumplir - si salimos con el break, no se ejecuta
    print("else")
print("Después")


