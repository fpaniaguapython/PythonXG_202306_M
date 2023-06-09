'''
Representar un relación de 3 Series de TV que está compuesta por:
- Título
- Calificación (int)
- La relación de actores
    - Nombre del actor
    - Nacionalidad
'''
series = [("S1",3,[('A1','N1'),('A2','N2'),('A3','N3')]),
          ("S2",7,[('A2','N2'),('A4','N4'),('A3','N3'),('A8','N8')]),
          ("S3",1,[('A3','N3'),('A5','N5')])]

nueva_serie = ("S4",8,[('A10','N10')])

series.append(nueva_serie)

print(series)

print(series[1][2][1][0])#A4
#series[1][2][1][0]='A15'#ERROR, LA TUPLA NO SE PUEDE MODIFICAR
series[1][2][1]=('A15','N15')
print(series[1][2][1][0])#A15

#Agregando un nuevo actor a S2, modificando el contenido de la lista pero no la tupla de actores
series[1][2].append(('Edurne','España'))
print(series)

