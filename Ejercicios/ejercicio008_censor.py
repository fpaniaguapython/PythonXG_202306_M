fichero = open('palabras_prohibidas.txt',mode='r',encoding="UTF-8")
palabras_prohibidas = [palabra_limpia.replace('\n','') for palabra_limpia in fichero.readlines()]#Comprensión de listas
fichero.close()

tweet = input("Introduce el texto del tweet:") 

#Utilizando el operador in, comprobar si el texto contiene alguna de las palabras prohibidas 
# (no importa mayúsculas ni minúculas)

#Quiero que recorras palabras_prohibidas
#y que en cada iteracción palabra_prohibida tenga el valor de
#la palabra prohibida de esa iteracción
for palabra_prohibida in palabras_prohibidas:
    if palabra_prohibida.upper() in tweet.upper():
        print("No puedes utilizar la palabra", palabra_prohibida)
        posicion = tweet.upper().index(palabra_prohibida.upper())
        palabra_prohibida_original = tweet[posicion:posicion+len(palabra_prohibida)]
        tweet = tweet.replace(palabra_prohibida_original, "*****")
print(tweet)