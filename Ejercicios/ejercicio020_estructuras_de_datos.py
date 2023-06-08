lista = [3,8,9,10,8.5,True,["Hola","Hello"]]
print(len(lista))#Longitud de la lista
print(lista[3])#Muestra la cuarta posición
lista.append("Final")
print(lista)
lista.insert(0,"Principio")
print(lista)#Lista completa
print(lista[1:-1])#Lista sin primero ni último
lista[3]="Nueve"#Modificación de un elemento
print(lista)

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2 #Genera una lista nueva con todos los elementos
print(l3)

print("Antes del pop:", lista)
ultimo = lista.pop()
print(ultimo)
print("Después del pop:", lista)

print("Antes del pop:", lista)
ultimo = lista.pop(0)
print(ultimo)
print("Después del pop:", lista)

print('Recorrer la lista:')
for item in lista:
    print(item)

print("**REMOVE**")#Elimina el primer elemento de la lista
lista.append('Nueve')
print(lista)
lista.remove('Nueve')
print(lista)






