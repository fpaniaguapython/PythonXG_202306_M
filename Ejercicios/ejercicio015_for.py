dorsales = [3,8,10,15,20]

for dorsal in dorsales:
    print(dorsal)

for dorsal in dorsales:
    print(dorsal)
else:#Sólo si el bucle termina; No se ejecuta con break
    print("Fin del for 1")

for dorsal in dorsales:
    print(dorsal)
    if dorsal==10:
        break
else:#Sólo si el bucle termina; No se ejecuta con break
    print("Fin del for 2")

for numero in range(0,100):#De 0 a 99, de 1 en 1
    print(numero, end="-")

print()

for numero in range(0,100,2):#De 0 a 99, de 2 en 2
    print(numero, end="-")

print()

for numero in range(100,0,-1):#De 100 a 1, de -1 en en -1
    print(numero, end="-")

print()

for numero in range(100):#De 0 a 99, de 1 en 1
    print(numero, end="-")

print()
#Comprensión de listas NIVEL 1
#Los números del 0 al 9
lista_10_enteros = [numero for numero in range(10)]
print(lista_10_enteros)
#Los números del 0 al 9 multiplicados por 2 (10 primeros pares)
lista_10_pares = [numero*2 for numero in range(10)]
print(lista_10_pares)

nombres = ["Edurne", "Fernando", "Alexander", "Jhoendris"]
#Los nombres convertidos a mayúsculas
nombres_mayusculas = [nombre.upper() for nombre in nombres]
print(nombres_mayusculas)

nombres = ["Edurne", "Fernando", "Alexander", "Jhoendris"]
#Los nombres a partir de la posición 2 convertidos a minúsculas
nombres_minusculas = [nombre.lower() for nombre in nombres[2:]] 
print(nombres_minusculas)

