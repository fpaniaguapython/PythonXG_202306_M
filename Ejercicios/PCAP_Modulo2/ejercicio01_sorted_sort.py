#¿sorted vs sort?

#Función sorted() → Genera una nueva lista ordenada.
#Método sort() → Ordena la lista.

lista1 = [10,3,4,5,8]
lista1.sort()
print(lista1)

lista1 = [10,3,4,5,8]
lista2 = sorted(lista1)
print(lista1)
print(lista2)

#Calcula la valoración del ítem de cara a la ordenación 
def valorar(item):
    return len(item[1])

lista = [(3,'Zaragoza'),(1,'Teruel'),(4,'Huesca')]
lista.sort(key=valorar, reverse=True)
print(lista)
