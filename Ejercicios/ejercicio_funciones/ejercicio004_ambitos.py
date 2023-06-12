#Paso de parámetros por valor (se modifica la copia)
def hacer(x):
    x=x+1
    print(x)#6
x = 5
hacer(x)
print(x)#5

#Paso de parámetros por referencia (se modifica todo)
def mover(y):
    y[0]=10
    print(y)#Daniel(10,2)
y = [1,2]
mover(y)
print(y)#Daniel(10,2)

#Paso de parámetros por valor (str)
def hacer(x):
    x="Adios"
    print(x)#Adios
x = "Hola"
hacer(x)
print(x)#Hola