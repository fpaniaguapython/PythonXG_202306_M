pelis = ["La Matanza de Texas", "Posesión Infernal", "House of the Haunted Hill", "Tiburón", "Alien"]

print(pelis)
pelis.sort()#Ordena la lista
print(pelis)

pelis = ["La Matanza de Texas", "Posesión Infernal", "House of the Haunted Hill", "Tiburón", "alien"]

print(pelis)
pelis.sort()#Ordena la lista
print(pelis)


ciudades = [('Vigo', 300_000), ('Pontevedra', 800_000), ('Santiago de Compostela', 100_000)]
print(ciudades)
ciudades.sort()
print(ciudades)

ciudades = [(300_000, 'Vigo'), (800_000, 'Pontevedra'), (100_000, 'Santiago de Compostela')]
print(ciudades)
ciudades.sort()
print(ciudades)


def valorar_ciudad(ciudad):
    return ciudad[1]

ciudades = [('Vigo', 300_000), ('Pontevedra', 800_000), ('Santiago de Compostela', 100_000)]
print(ciudades)
ciudades.sort(key=valorar_ciudad)
print(ciudades)

#Título, Calificación, Número de temporadas
def calificador_series(serie):
    return serie[2]

series = [("Los Soprano", 5, 10), ("House", 4, 8), ("Los Simpsons", 5, 29)]
series.sort(key=calificador_series)#Ordena por número de temporadas, de menor a mayor
series.reverse()#Invierte el orden, de mayor a menor número de temporadas
print(series)

#Restaurante: Nombre, Calidad, Ubicación, Precio
def calificador_restaurantes(restaurante):
    #Va a calificar cada restaurante con Calidad*3 + Ubicacion*1 + Precio*2
    calificacion = restaurante[1]*3+restaurante[2]*1+restaurante[3]*2
    print(restaurante[0],calificacion)#Muestra la calificación del restaurante actual
    return calificacion

restaurantes = [("R1",10,3,8),("R2",5,6,5),("R3",10,9,1),("R4",8,8,8)]
restaurantes.sort(key=calificador_restaurantes, reverse=True)
print(restaurantes) #[('R1', 10, 3, 8), ('R4', 8, 8, 8), ('R3', 10, 9, 1), ('R2', 5, 6, 5)]
#Mostrar cuál es el mejor restaurante
print("Restaurante elegido:", restaurantes[0][0]) #Restaurante elegido: R1
