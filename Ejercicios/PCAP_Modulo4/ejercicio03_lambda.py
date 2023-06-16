#Lambda sin parámetros
f1 = lambda : 2 #Devuelve 2
print(f1())

#Lambda con un parámetro
f2 = lambda x : x * 2#Devuelve el parámetro x multiplicado por 2 
print(f2(4))

#Lambda con varios parámetro
f3 = lambda x, y : x + y#Devuelve el parámetro x + parámetro y
print(f3(4,3))

#Aplicación de una lambda en una función sorted
lenguajes = [('Python',3_000),('Java',8_000),('C',2_500),('Kotlin',1_800)]
print(sorted(lenguajes, key=lambda lenguaje : lenguaje[1]))

#filter sin lambda
def contiene_o(lenguaje):
    return 'o' in lenguaje[0]

filter_contiene_o = filter(contiene_o, lenguajes)
lista_contiene_o = list(filter_contiene_o)
print("Contiene o:",lista_contiene_o)

#filter con lambda
filter_mayores_2800 = filter(lambda lenguaje : lenguaje[1]>=2800, lenguajes)
lista_mayores_2800 = list(filter_mayores_2800)
print("Más de 2800 usuarios:", lista_mayores_2800)

#map sin lambda
lenguajes = [('Python',3_000),('Java',8_000),('C',2_500),('Kotlin',1_800)]

def calcular_ratio(lenguaje):
    return len(lenguaje[0]*lenguaje[1])

map_ratio = map(calcular_ratio, lenguajes)#Devuelve un map (generador iterable)
lista_ratio = list(map_ratio)
print(lista_ratio)

#map con lambda
lenguajes = [('Python',3_000),('Java',8_000),('C',2_500),('Kotlin',1_800)]

map_ratio_lambda = map(lambda lenguaje : len(lenguaje[0]*lenguaje[1]), lenguajes)#Devuelve un map (generador iterable)
lista_ratio_lambda = list(map_ratio_lambda)
print(lista_ratio_lambda)