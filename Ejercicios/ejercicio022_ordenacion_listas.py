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
