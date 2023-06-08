#Crear un lista con 3 títulos película
peliculas = ["El Resplandor","La Cosa","La Momia"]
print(peliculas)
#Pedir al usuario un nuevo título e insertarlo al principio de la lista (insert)
titulo = input("Título(insert):")
peliculas.insert(0,titulo)
print(peliculas)
#Pedir al usuario un nuevo título e insertarlo al final de la lista (append)
titulo = input("Título(append):")
peliculas.append(titulo)
print(peliculas)
#Pedir al usuario un título y modificar el tercer elemento de la lista ([indice]='nuevo valor')
titulo = input("Título(modificación):")
peliculas[2]=titulo
print(peliculas)

#while (mientras que la lista tenga películas)
    #Pedir al usuario un título y eliminarlo de la lista (remove)
while len(peliculas)>0:
    titulo = input("Título(eliminación):")
    try:
        peliculas.remove(titulo)#Raises ValueError if the value is not present.
    except:
        print("No se ha encontrado la película")
    print(peliculas)
else:
    #Escribir la lista está vacía
    print("La lista está vacía")



