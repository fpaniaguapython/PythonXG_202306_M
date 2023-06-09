def calidad(restaurante):
    return restaurante[1]#Devuelve la calidad

#Restaurante: Nombre, Calidad, Ubicación, Precio
restaurantes = [("R4",8,8,8),("R1",10,3,8),("R2",5,6,5),("R3",9,9,1)]

print(max(restaurantes))
print(min(restaurantes))

print(max(restaurantes, key=calidad))
print(min(restaurantes, key=calidad))