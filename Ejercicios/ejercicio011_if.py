EDAD_MINIMA = 18
EDAD_JUBILACION = 65
ALTURA_MINIMA = 178

edad = 68
altura = 180


if edad<EDAD_MINIMA:
    print("Eres menor de edad")

if edad<EDAD_MINIMA: print("Eres menor de edad")

if edad<EDAD_MINIMA:
    print("ERROR")
    print("Eres menor de edad")

if edad<EDAD_MINIMA: print("ERROR"); print("Eres menor de edad")

if edad<EDAD_MINIMA:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

if edad<EDAD_MINIMA:
    print("Eres menor de edad")
elif edad>EDAD_JUBILACION:
    print("Te puedes jubilar")

if edad<EDAD_MINIMA:
    print("Eres menor de edad")
elif edad>EDAD_JUBILACION:
    print("Te puedes jubilar")
else:
    print("Estás en tierra de nadie")


if edad>=EDAD_MINIMA:
    if edad>EDAD_JUBILACION:
        print("Estás en edad de jubilarte")
    elif edad<40:
        print("Te toca contribuir")
    else:
        print("No sé qué pasa")
else:
    print("ERES MENOR DE EDAD")


#OPERADOR TERNARIO
#Forma 'tradicional'
if edad>EDAD_JUBILACION:
    jubilado = True
else:
    jubilado = False

#Forma 'ternaria'
jubilado = True if edad>EDAD_JUBILACION else False

#Forma 'turbo'
jubilado = edad>EDAD_JUBILACION

#EJERCICIO
#Si la edad es > 40, salario bruto anual de 25_000, si no, 18_000
edad = 38

if edad > 40:
    salario_bruto = 25_000
else:
    salario_bruto = 18_000

salario_bruto = 25_000 if edad > 40 else 18_000

print(f'Tu salario bruto anual es de {salario_bruto}')#f-string

