#Closure - Nivel 1
def funcion_externa():
    def funcion_interna():
        print("Hola")
    return funcion_interna

resultado = funcion_externa()
resultado()

#Closure - Nivel 2
def funcion_externa(lista_compra):
    lista_productos = lista_compra.copy()
    def funcion_interna():
        for producto in lista_productos:
            print('Producto:', producto)
    return funcion_interna

cesta = ['Pan','Aceite','Vino']
visualizador = funcion_externa(cesta)
cesta.append('Leche')
visualizador()


#Aplicación de closure con decorador
#https://realpython.com/primer-on-python-decorators/

def asteriscador(func):
    def inner_function(numero):
        print("***************")
        func(numero)
        print("***************")
    return inner_function

@asteriscador
def mostrar_resultado(numero):
    print("El resultado es",numero)

mostrar_resultado(10)

