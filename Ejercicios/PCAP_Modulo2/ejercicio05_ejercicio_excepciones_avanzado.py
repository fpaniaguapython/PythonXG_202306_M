'''
Crear la función 'validar' que recibe los siguientes parámetros:
- Nombre. Debe ser un str y debe tener más de 10 caracteres de longitud.
- Email. Debe tener una letra @, un ., y más de 5 caracteres de longitud.
- Año de nacimiento. Debe ser un entero entre 1900 y 2023.

La función debe impedir que entre parámetros que no cumplan con las reglas.
'''
class EmailException(BaseException):
    pass


LONGITUD_MINIMA_NOMBRE = 11
LONGITUD_MINIMA_EMAIL = 6
ANHO_MINIMO = 1900
ANHO_MAXIMO = 2023

def __validar_nombre(nombre):
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser un str")
    if len(nombre)<LONGITUD_MINIMA_NOMBRE:
        raise ValueError("La longitud del nombre de ser > " + str(LONGITUD_MINIMA_NOMBRE-1)) 

def __validar_email(email):
    if not isinstance(email, str):
        raise TypeError("El email debe ser un str")
    if email.count('@')!=1 or '.' not in email:
        raise EmailException("El email debe contener un único símbolo @ y al menos un .")
    if len(email)<LONGITUD_MINIMA_EMAIL:
        raise ValueError("La longitud del email de ser > " + str(LONGITUD_MINIMA_EMAIL-1))

def __validar_anho(anho):
    if not isinstance(anho, int):
        raise TypeError("El año debe ser entero")
    if not (anho>=ANHO_MINIMO and anho<=ANHO_MAXIMO):
        raise ValueError(f'El año debe estar entre {ANHO_MINIMO} y {ANHO_MAXIMO}')

def validar(nombre : str, email : str, anho : int):
    #Validación del nombre
    __validar_nombre(nombre)
    #Validación del email
    __validar_email(email)
    #Validación del año
    __validar_anho(anho)
  

#Introducción de datos
'''
try:
    nombre = input("Nombre:")
    email = input("email:")
    anho = int(input("Año:"))
except ValueError:
    print("El año introducido no tiene el tipo correcto")
'''
    

#Validación de datos
try:
    #validar(nombre,email,anho)
    validar("Fernando Paniagua","fernando.paniagua$gmail.com",1971)
except TypeError as exception:
    print(exception)
except ValueError as exception:
    print(exception)
except EmailException:#Una exception propia
    print("¡EL EMAIL ESTÁ MAL CONSTRUIDO!")
else:
    print("OK")