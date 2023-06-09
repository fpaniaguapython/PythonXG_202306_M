#pip install requests
import json
import requests
import ejercicio030_motor_locucion

KEY='95c08eba'

if __name__=='__main__':
    titulo = input("Introduce un título:")
    parametros = {'apikey':KEY, 't': titulo} 
    r = requests.get('http://www.omdbapi.com/', params=parametros)
    if r.status_code==200:
        #OK
        #print(r.text)
        diccionario_datos = json.loads(r.text)#Convertir el str (en formato json) a dictionariy
        
        #Obtiene la sinopsis y la narra a través de gTTS
        #sinopsis = diccionario_datos["Plot"]
        #ejercicio030_motor_locucion.narrar(sinopsis)

        #Mostrar por pantalla:
        #Título
        #Director
        #Fecha de estreno
        #Sinopsis
        #Actores de uno en uno
        
    else:
        #ERROR
        print("ERROR:", r.status_code)


