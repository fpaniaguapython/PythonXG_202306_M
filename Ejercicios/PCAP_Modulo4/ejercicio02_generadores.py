#Generador manual
def generardor():
    for numero in range(100):
        yield numero #yield hace que la función funcione como un iterador
    
for numero_generado in generardor():
    print(numero_generado)


#Generador mediante 'comprensión de listas'
#Conversión 'tradicional' -> Genera dos listas
estaciones = ["Primavera","Verano","Otoño","Invierno"]
estaciones_mayusculas = [estacion.upper() for estacion in estaciones]
print(estaciones_mayusculas)
#Conversión mediante generador
estaciones = ["Primavera","Verano","Otoño","Invierno"]
estaciones_minusculas = (estacion.lower() for estacion in estaciones)#Proporciona un generador
print(estaciones_minusculas)#Es un iterador, NO una lista
for estacion_minusculas in estaciones_minusculas:
    print(estacion_minusculas)


