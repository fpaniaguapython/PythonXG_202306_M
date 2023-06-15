'''
clase - gato
instancia u objeto - jara
clase -> objeto - instanciar o crear un objeto (de forma implícita a través del constructor)
clase:
    atributos:
        nombre, color_pelo, malhumorado, posicion(x,y,z)
    métodos:
        andar, saltar, comer, ...

__init__ -> constructor 
'''

class Gato:
    def __init__(self, _nombre : str, _color_pelo : str, _malhumorado : bool, _posicion : tuple) -> None:
        print("Ejecutando __init__ de Gato...")
        self.nombre = _nombre #self.nombre -> atributo ; _nombre -> parámetro del constructor
        self.color_pelo = _color_pelo
        self.malhumorado = _malhumorado
        self.posicion = _posicion
        self.cansancio = 0 #Atributo cuyo valor inicial no viene como parámetro
        self.__vivo = True
    def andar(self, delta_x, delta_z):
        print(f'Soy {self.nombre} y estoy andando...')
        self.posicion = (self.posicion[0]+delta_x, self.posicion[1], self.posicion[2]+delta_z)
        self.cansancio+=1
    def saltar(self):
        pass
    def comer(self, latas):
        print(f'Soy {self.nombre} y estoy comiendo...')
        self.cansancio=self.cansancio-latas
        if self.cansancio<0 : self.cansancio=0


#Instanciar un gato
gato1 = Gato("Jara","Pardo",True,(4,0,2))#Instanciar: gato1 es el nombre del objeto
print(gato1.posicion)#Acceso al atributo
print(gato1.cansancio)
gato1.andar(0,1)#Invocar un método
print(gato1.posicion)#Acceso al atributo
print(gato1.cansancio)

#Dar de comer al gato cualquier número de latas de comida para gato.
#Cada lata de comida para gato decrementa el cansancio en 1 unidad.
#El gato no puede tener cansancio <0
gato1.comer(2)
print(gato1.cansancio)

#Instanciar otro gato
#Moverse 1 hacia la derecha y 1 hacia atrás, en dos pasos
#Dar de comer para que recuper las energías.

gato2 = Gato("Torpe","Negro","False",(3,0,1))
gato2.andar(1,0)
gato2.andar(0,-1)
print(gato2.posicion)
print(gato2.cansancio)
gato2.comer(2)
print(gato2.cansancio)


#Atributo __dict__
#Proporciona un diccionario con todos los atributos del objeto, incluyendo su valor
#Incluye los ocultos renombrados
print(gato1.__dict__)
for k,v in gato1.__dict__.items():
    print(k,":",v)





