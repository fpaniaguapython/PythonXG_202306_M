#Función sin argumentos y sin retorno
def escribir_algo():
    print("Algo")

#Función con argumentos y sin retorno
def escribe_un_numero_concreto(numero):
    print(numero)

#Función con dos argumentos y con retorno
def sumar(s1, s2):
    resultado = s1 + s2
    return resultado 

escribir_algo()
escribe_un_numero_concreto(8)
sumar(3,2)
resultado = sumar(3,2)

#Función con llamada con parámetros por nombre
def elevar(n1, n2):
    resultado = n1**n2
    return resultado

r = elevar(2,3)#Uso de argumentos posicionales
print("Resultado:", r)

r = elevar(n2=2, n1=3)
print("Resultado:", r)

#Mejorando la lectura del código
def calcular_coeficiente(base, porcentaje, ratio, correccion, delta, multiplicador):
    pass
calcular_coeficiente(base=3000, ratio=4, porcentaje=3, correccion=10.3, delta=-2, multiplicador=8)

#Función con parámetros con valores por defecto (opcionales)
def calcular(x, y=-5.3, z=0):
    print(x, y, z)

calcular(3,4,8)
calcular(3,4)#(Posicional) Asignación a y
calcular(3,z=4)#(Por nombre) Asignación a z
calcular(3)

'''
#ERROR_ Los valores por defecto SIEMPRE tienen que ir a la derecha
def calcular(x=8, y, z=0):
    print(x, y, z)
'''

#Funciones con número indeterminado de parámetros (recibe tupla)
def sumar(*sumandos):
    print(sumandos)#(3, 8, 10, 15)
    print(type(sumandos))#<class 'tuple'>

sumar(3, 8, 10, 15)

#Funciones con número indeterminado de parámetros con valores por defecto
def sumar(*sumandos, corrector=True):
    print(sumandos)
    print(type(sumandos))#<class 'tuple'>
    resultado = sum(sumandos)
    print("Resultado de sum:",resultado)

sumar(3, 8, 10, False)
sumar(3, 8, 10, corrector=False)

#Funciones con número interderminado de parámetros (recibe diccionario)
def calcular(**kwargs):
    print(type(kwargs))#<class 'dict'>
    print(kwargs)#{'s1': 5, 's3': 8, 's4': 10}

calcular(s1=5, s3=8, s4=10)


















