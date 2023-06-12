print("Modulo 2")

#Todas las entidades
import modulo1
print(modulo1.nombre_m1)
modulo1.f1_1()

#Varias entidades
from modulo1 import nombre_m1, f1_1
print(nombre_m1)
f1_1()

#Todas las entidades - con alias
import modulo1 as supermodulo
print(supermodulo.nombre_m1)
supermodulo.f1_1()

#Varias entidades - con alias
from modulo1 import nombre_m1 as nm1, f1_1 as f11
print(nm1)
f11()

#Todas las entidades con * (evita tener que referenciar al espacio de nombres)
from modulo1 import *

'''
import modulo1 -> modulo1.f1_1()
from modulo1 import * -> f1_1()
'''







