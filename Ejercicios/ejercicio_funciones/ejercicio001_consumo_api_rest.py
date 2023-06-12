import requests

KEY='95c08ebax'


def procesar_pelicula(pelicula):
    titulo = pelicula["Title"]
    director = pelicula["Director"]
    fecha_de_estreno = pelicula["Released"]
    sinopsis = pelicula["Plot"]
    
    actores = [actor.strip() for actor in pelicula["Actors"].split(',')]
    
    print(titulo)
    print(director)
    print(fecha_de_estreno)
    print(sinopsis)
    for actor in actores:
        print("Actor:",actor)

if __name__=='__main__':
    titulo = input("Introduce un título:")
    parametros = {'apikey':KEY, 't': titulo} 
    r = requests.get('http://www.omdbapi.com/', params=parametros)
    if r.status_code==200:
        diccionario_datos = r.json()#Obtiene directamente un diccionario
        procesar_pelicula(diccionario_datos)
    elif r.status_code==401:
        #ERROR DE CLAVE INCORRECTA
        print("ERROR: Clave incorrecta", r.status_code)
    else:
        #ERROR
        print("ERROR:", r.status_code)