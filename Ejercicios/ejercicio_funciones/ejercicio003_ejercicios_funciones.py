#Muestra 'Hola' por pantalla
def mostrar_hola():
    pass

#Muestra 'Hola' a una persona concreta
def mostar_hola_usuario(nombre_usuario):
    print("Hola",nombre_usuario)

#Genera un texto saludando a una persona concreta
def generar_hola_usuario(nombre_usuario):
    saludo = f'Hola {nombre_usuario}'
    return saludo

#Suma dos números
def suma_dos_numeros(sumando1, sumando2):
    return sumando1+sumando2

#Suma un número indeterminado de números
def suma_numeros(*numeros):
    return sum(numeros)

#Escribe un texto en un fichero
def escribe_en_fichero(nombre_fichero, texto):
    pass

#Obtiene el valor de una clave a partir de un diccionario
def get_valor_diccionario(diccionario, clave):
    return

#Escribe los datos de una persona en un fichero PDF
#Recibiendo una estructura tipo lista, tupla o diccionario
def escribir_pdf(datos, fichero_pdf):
    print("Función 1")
    pass

#Escribe los datos de una persona en un fichero PDF
#Recibiendo una sucesión de parámetros
def escribir_pdf(datos, fichero_pdf):
    print("Función 2")
    pass

#NOTA: De las dos funciones escribir_pdf, sobrevive la última
escribir_pdf("x","y")#Ejecuta la función 2

#Escribe los datos de una persona en un fichero PDF
#Recibiendo una sucesión de parámetros
def escribir_pdf(*datos, fichero_pdf):
    print("Función 3")
    pass

#NOTA: De las tres funciones escribir_pdf, sobrevive la última
escribir_pdf("x",fichero_pdf="y")#Ejecuta la función 3