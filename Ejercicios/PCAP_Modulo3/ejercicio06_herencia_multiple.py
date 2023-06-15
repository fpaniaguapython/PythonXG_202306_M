class Vehiculo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def avanzar(self):
        print(f'Soy Vehiculo {self.nombre} y estoy avanzando')
    def m1(self):
        print("Método 1")

class Automovil(Vehiculo):
    def avanzar(self):
        print(f'Soy Automovil {self.nombre} y estoy avanzando')
    def m2(self):
        print("Método 2")

class Barco(Vehiculo):
    def avanzar(self):
        print(f'Soy Barco {self.nombre} y estoy avanzando')
    def m3(self):
        print("Método 3")

class Anfibio(Automovil, Barco):
    def avanzar(self):
        print(f'Soy Anfibio {self.nombre} y estoy avanzando')
    def m4(self):
        print("Método 4")

v = Anfibio("x13j")#Tiene toda la funcionalidad y atributos heredados de todas las superclases
v.avanzar()

#Opciones a la hora de modificar un atributo
v.nombre = "el barco de chanquete" #Método tradicional 
setattr(v, "nombre", "el barco de chanquete")#A través de setattr

#Opcinoes a la hora de leer un atributo
print(v.nombre) #Método tradicional 
print(getattr(v, 'nombre')) #A través de getattr

#issubclass
print(issubclass(Anfibio, Barco))#True
print(issubclass(Automovil, Barco))#False
print(issubclass(Automovil, Vehiculo))#True
print(issubclass(Anfibio, Vehiculo))#True

#isinstance
print(isinstance(v,Anfibio))#True
print(isinstance(v,Automovil))#True
print(isinstance(v,Barco))#True
print(isinstance(v,Vehiculo))#True
