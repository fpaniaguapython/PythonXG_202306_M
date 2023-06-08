edad = 35

match edad:
    case 10:
        print("Tienes 10 años")
    case 25:
        print("Tienes 25 años")
    case other:#Es igual que poner 'case _'
        print("No sé qué pasa")


match edad:
    case 10:
        print("Tienes 10 años")
    case 25:
        print("Tienes 25 años")
    case _:#Igual que poner 'case other'
        print("No sé qué pasa")

nombre = "Fernando"

match nombre:
    case "Fernando":
        print("¡Bien!")
    case other:
        print("¡Mejorable!")


#Python - Creado en 1991
#Java - Creado en 1996
#C# - Creado en 2000
#R - Creado en 1993
#other - No dispongo de información

#Pedir al usuario que introduzca un nombre de lenguaje de programación
#Mostrar la información de cuando fue creado o el valor por defecto
#No debe afectar si lo escribe en mayúsculas o minúsculas

lenguaje = input("Introduce un nombre de lenguaje:")

match lenguaje.upper():
    case "PYTHON":
        print("Creado en 1991")
    case "JAVA":
        print("Creado en 1996")
    case "C#":
        print("Creado en 2000")
    case "R":
        print("Creado en 1993")
    case _:
        print("No dispondo de información")




