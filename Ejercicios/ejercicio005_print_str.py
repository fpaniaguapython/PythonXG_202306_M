frase = "Me gusta tomar el 'café' sólo"
frase = 'No me gusta la leche en el "café"'
frase = "El \"café\" descafeinado no sabe igual que el normal" #Escapando las comillas dobles
frase = 'El \'café\' descafeinado no sabe igual que el normal' #Escapando las comillas simples
nombre = "Alberto"
edad = 34
origen = "Galicia"

print()
print(frase)
print(nombre, edad)
print(nombre, edad, sep="##")
print(nombre, end="-")
print(edad)

print(nombre, edad, sep="-", end="-Origen:")
print(origen)
#Alberto-34-Origen:Galicia

#Solicitar al usuario su nombre
#Solicitar al usuario su ciudad de residencia
#Solicitar al usuario su dirección de correo electrónico
#Mostrar el texto equivalente a: Me llamo Fernando, resido en Madrid y mi email es fernando.paniagua@gmail.com
nombre = input("Nombre:")
ciudad = input("Ciudad de residencia:")
email = input("Correo electrónico:")
print("Me llamo ",nombre,", resido en ",ciudad," y mi email es ",email,sep="")
#Solución f-string
cadena = f'Me llamo {nombre.upper()}, resido en {ciudad} y mi email es {email}'
print(cadena)

cadena = 'Esta frase \'tiene\' comillas \ny tienes varias\t\t\t líneas'
print(cadena)

cadena = 'Lo que sea'
cadena_multiple = '''Línea 1
Línea 2
Línea 3
Línea 4'''
print(cadena_multiple)

'''
Comentario múltiples líneas
Línea comentario 2
Línea comentario 3
'''












