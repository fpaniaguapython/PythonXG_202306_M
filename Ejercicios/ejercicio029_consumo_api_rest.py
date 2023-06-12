#pip install requests
#import json
import requests
import ejercicio030_motor_locucion

KEY='95c08ebax'

if __name__=='__main__':
    titulo = input("Introduce un título:")
    parametros = {'apikey':KEY, 't': titulo} 
    r = requests.get('http://www.omdbapi.com/', params=parametros)
    if r.status_code==200:
        #OK
        #print(r.text)
        #diccionario_datos = json.loads(r.text)#Convertir el str (en formato json) a dictionariy
        diccionario_datos = r.json()#Obtiene directamente un diccionario
        
        #Obtiene la sinopsis y la narra a través de gTTS
        #sinopsis = diccionario_datos["Plot"]
        #ejercicio030_motor_locucion.narrar(sinopsis)

        #Mostrar por pantalla:
        #Título
        #Director
        #Fecha de estreno
        #Sinopsis
        #Actores de uno en uno
        titulo = diccionario_datos["Title"]
        director = diccionario_datos["Director"]
        fecha_de_estreno = diccionario_datos["Released"]
        sinopsis = diccionario_datos["Plot"]
        '''
        actores = diccionario_datos["Actors"].split(',')
        actores = [actor.strip() for actor in actores]
        '''
        actores = [actor.strip() for actor in diccionario_datos["Actors"].split(',')]
        print(titulo)
        print(director)
        print(fecha_de_estreno)
        print(sinopsis)
        for actor in actores:
            print("Actor:",actor)
    elif r.status_code==401:
        #ERROR DE CLAVE INCORRECTA
        print("ERROR: Clave incorrecta", r.status_code)
    else:
        #ERROR
        print("ERROR:", r.status_code)


