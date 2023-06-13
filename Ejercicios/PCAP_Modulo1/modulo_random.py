import random
from math import floor

#
# random.random()
#
for i in range(10):
    x = random.random()#float en el rango[0,1)
    print(x)

#Entre 0 y 100
random.random()*100 #[0,100)

#
# random.seed()
#
random.seed()
print("Semilla del reloj:",random.random())

random.seed(2023)
print("Semilla concreta:",random.random())
print("Semilla concreta:",random.random())
print("Semilla concreta:",random.random())

#
# random.randrange(10)
#
random.seed()
x = random.randrange(100)#[0,100) de 1 en 1
print(x)
x = random.randrange(10,20,2)#[10,20) sólo los pares
print(x)

#
# random.randint()
#
x = random.randint(10,20)#[10,20] (ambos incluídos)
print(x)

#
# random.choise(iterable)
#
lista = ['Primavera','Verano','Otoño','Invierno']
x = random.choice(lista)
print(x)

#
# random.sample(iterable, numero_elementos)
#
lista = ['Primavera','Verano','Otoño','Invierno']
x = random.sample(lista, 2)#Ejemplo: ['Invierno', 'Primavera']
print(x)




