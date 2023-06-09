diccionario = {15:"Andrés",2:"Edurne",3:"Daniel",4:"Óscar",5:"Alberto"}

print(len(diccionario))

print(diccionario[15])#Andrés
print(diccionario.get(2))#Edurne

#print(diccionario[12])#KeyError
print(diccionario.get(12))#None
print(diccionario.get(12,"No sé"))#No sé (Valor por defecto)

#Recorrer las claves
for clave in diccionario.keys():
    print(clave)

#Recorrer los valores
for valor in diccionario.values():
    print(valor)

#Recorrer las claves,valores
for clave,valor in diccionario.items():
    print(clave,":",valor)

diccionario[2]="Jero"#Modificación
print(diccionario)

diccionario[100]="Edurne"#Insercción
print(diccionario)

diccionario[100]="Jhoendris"#Modificación
print(diccionario)

diccionario["Jero"]="Jero"
print(diccionario)#{15: 'Andrés', 2: 'Jero', 3: 'Daniel', 4: 'Óscar', 5: 'Alberto', 100: 'Jhoendris', 'Jero': 'Jero'}

elemento_2=diccionario.pop(2)#Devuelve el valor del item con key 2 y lo elimina
print(elemento_2)#Jero
print(diccionario)#{15: 'Andrés', 3: 'Daniel', 4: 'Óscar', 5: 'Alberto', 100: 'Jhoendris', 'Jero': 'Jero'}

elemento_ultimo=diccionario.popitem()#Devuelve el último item completo (clave y valor) y lo elimina
print(elemento_ultimo)#('Jero', 'Jero')
print(diccionario)#{15: 'Andrés', 3: 'Daniel', 4: 'Óscar', 5: 'Alberto', 100: 'Jhoendris'}

'''
Representar un relación de 3 Series de TV que está compuesta por:
- Título
- Calificación (int)
- La relación de actores
    - Nombre del actor
    - Nacionalidad
'''

'''
series = [("S1",3,[('A1','N1'),('A2','N2'),('A3','N3')]),
          ("S2",7,[('A2','N2'),('A4','N4'),('A3','N3'),('A8','N8')]),
          ("S3",1,[('A3','N3'),('A5','N5')])]
'''

series = { "S1":{"Calificacion":3,"Actores":[{"Nombre":'A1',"Nacionalidad":'N1'},{"Nombre":'A2',"Nacionalidad":'N2'},{"Nombre":'A3',"Nacionalidad":'N3'}]},
           "El Resplandor":{"Calificacion":7,"Actores":[{"Nombre":'A2',"Nacionalidad":'N2'},{"Nombre":'Jack Nicholson',"Nacionalidad":'Estadoudiense'},{"Nombre":'A3',"Nacionalidad":'N3'},{"Nombre":'A8',"Nacionalidad":'N8'}]},
           "S3":{"Calificacion":1,"Actores":[{"Nombre":'A3',"Nacionalidad":'N3'},{"Nombre":'A5',"Nacionalidad":'N5'}] }}

print(series["El Resplandor"]["Calificacion"])
print(series["El Resplandor"]["Actores"][1]["Nombre"])
