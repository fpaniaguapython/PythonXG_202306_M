def eco(numero, retorno):
    print("Función:", numero)
    return retorno

#Si la primera parte es False no se evalua la segunda
if eco(1,False) and eco(2,True):
    print("OK")
else:
    print("KO")

#Si la primera parte es True, no se evalua la segunda
if eco(3,True) or eco(4,True):
    print("OK")
else:
    print("KO")


#Si la primera parte es True, no se evalua la segunda
primera_condicion = eco(5,True)
segunda_condicion = eco(6,True)

if primera_condicion or segunda_condicion:
    print("OK")
else:
    print("KO")


#Es mayor de edad, el nombre contiene la letra a, la direccion no puede ser Teruel
#(Debe medir mas de 1.50 o saber Japonés).
MAYORIA_EDAD = 16
LETRA_OBLIGATORIA = 'a'
DIRECCION_PROHIBIDA = 'Teruel'
ALTURA_MINIMA = 1.50

edad = 19
nombre = "Carmen"
direccion = "Teruel"
altura = 1.40
japones = True

#Solución 1
if edad >= MAYORIA_EDAD and (LETRA_OBLIGATORIA in nombre.lower()) and direccion != DIRECCION_PROHIBIDA and (altura > ALTURA_MINIMA or japones == True):
    print("OK")
else:
    print("KO")

#Solución 2
mayor_edad = edad>=MAYORIA_EDAD
contiene_a = LETRA_OBLIGATORIA in nombre.lower()
direccion_no_teruel = direccion!=DIRECCION_PROHIBIDA
altura_suficiente = altura > ALTURA_MINIMA

if mayor_edad and contiene_a and direccion_no_teruel and (altura_suficiente or japones):
    print("OK")
else:
    print("KO")

