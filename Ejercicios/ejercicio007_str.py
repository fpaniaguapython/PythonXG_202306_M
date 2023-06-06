cadena = "Me gusta tomar el café sólo y sin azúcar ni leche"
print(cadena[:])
#Mostrar utilizando slicing los 10 primeros caracteres
print(cadena[:10])
#Mostrar utilizando slicing los 10 últimos caracteres
print(cadena[-10:])
#Mostrar utilizando slicing los caracteres entre el 5 y 10 (ambos incluidos)
print(cadena[4:10])
#Al final, la cadena sigue como estaba
print(cadena)

#Dada la variable nombre_fichero, eliminar de la misma la extensión utilizando slicing
nombre_fichero = "amanecerprimaveral.jpg"
nombre_fichero = nombre_fichero[:-4]
print(nombre_fichero)

#Modificación para cualquier tamaño de extensión
nombre_fichero = "amanecerprimaveral.jpeg"
posicion_punto = nombre_fichero.find(".")
nombre_fichero = nombre_fichero[:posicion_punto]
print(nombre_fichero)

#Ejercicio:
#1. Solicitar al usuario una contraseña.
#2. Verificar que la contraseña no contiene la letra A. Utilizar el método count.
#3. Verificar que la contraseña tiene más de 4 caracteres.
#Si los puntos 2 y 3 están confirmados, la contraseña es válida.

password = input("Introduce tu contraseña:")
if (password.upper().count('A')>0):
    print("Error:")
    print("No puede contener letras A")
elif (len(password)<5):
    print("Error. Debe tener más de 4 caracteres")
else:
    print("La contraseña es correcta")

#Ejercicio:
#1. Solicitar al usuario un email.
#2. Verificar que el email contiene un símbolo @ (arroba) (método count)
#3. Verificar que el email contiene un símbolo . (punto) (método count)
#4. Verificar que el email tiene más de 10 caracteres. (función len)
#Si los puntos 2, 3 y 4 están confirmados, el email es válido.
email = input("Introduce el email:")
if email.count("@")!=1:
    print("Error. Debe contener únicamente una arroba")
elif email.count(".")==0:
    print("Error. Debe contener al menos un punto")
elif len(email)<=10:
    print("Error. Debe tener más de 10 caracteres")
else:
    print("La dirección es válida")

cadena="nombre"
respuesta=True
edad=19


