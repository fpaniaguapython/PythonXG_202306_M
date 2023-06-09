#conjunto1 = {}#Lo interpreta como un diccionario
conjunto1 = {'Elemento1'}
conjunto2 = set()

print(type(conjunto1))
print(type(conjunto2))


conjunto = {"Rojo","Verde","Azul","Amarillo","Verde","Blanco"}
print(conjunto)#{'Rojo', 'Azul', 'Verde', 'Amarillo', 'Blanco'}#Sin orden, sin duplicados
#print(conjunto[1])#ERROR
#conjunto[0:]#ERROR

print("Rojo" in conjunto)#True

#Métodos:
#isdisjoint -> Determina si dos conjuntos no tienen elementos en común.
#intersection -> Obtiene los elementos comunes a dos conjuntos
#difference -> Obtiene la diferencia de elementos

frutas_invierno = {"Naranja","Uva"}
frutas_verano = {"Sandía","Melón"}
frutas_invierno.isdisjoint(frutas_verano) #True, porque no tienen elementos comunes

frutas_verano = {"Sandía","Melón","Naranja"}
frutas_invierno = {"Naranja","Uva"}
frutas_verano.difference(frutas_invierno) #{'Sandía', 'Melón'}
frutas_invierno.difference(frutas_verano) #{'Uva'}


base_conocimiento = (("qué tiempo va a hacer hoy","Hoy va a a llover"), 
                     ("qué tiempo hace","Hoy va a a llover"),
                     ("dime el pronóstico del tiempo para hoy","Hoy va a a llover"),
                     ("qué hora es", "Son las 11:20"), 
                     ("cuál es la capital de alemania", "La capital de Francia es Berlín"),
                     ("cuál es la capital de francia", "La capital de Francia es París"))

pregunta = input("¿Qué quieres saber?")

coincidencias = 0

for conocimiento in base_conocimiento:
    conjunto_conocimiento = set(conocimiento[0].split())#Tomamos la pregunta de la base de conocimientos, la troceamos y la convertimos a conjunto
    conjunto_pregunta = set(pregunta.split())#Tomamos la pregunta del usuario, la troceamos y la convertimos en conjunto
    print("INTERSECCIÓN:", conjunto_conocimiento.intersection(conjunto_pregunta))
    coincidencias_actuales = len(conjunto_conocimiento.intersection(conjunto_pregunta))
    if coincidencias_actuales>coincidencias:
        mejor_respuesta = conocimiento[1]
        coincidencias = coincidencias_actuales

print(mejor_respuesta)