class Vehiculo(object):#Hereda de object
    def __init__(self, nombre, capacidad, velocidad_maxima, material) -> None:
        #Valores iniciales proporcionados por la llamada constructor
        self.nombre = nombre
        self.capacidad = capacidad
        self.velocidad_maxima = velocidad_maxima
        self.material = material #Plástico
        #Valores iniciales asignados desde dentro del constructor
        self.velocidad_actual = 0 #Km/hora
        self.carga_actual = 0 #Kilogramos
        #'protegido'
        self._aceleracion = 10 #m/s**2
        #'privado' u 'oculto'
        self.__consumo = 5 #l/100km
        self.__posicion = (0,0,0)

    def desplazar(self,x,y,z):
        pass

    def girar(self, grados):
        pass

class Avion(Vehiculo):
    def despegar(self):
        pass
    def aterrizar(self):
        pass


avion1 = Avion('F18',1000,2500,'Aluminio')
avion1.despegar()
avion1.desplazar(1,5,1)
print(avion1.nombre)
print(avion1._aceleracion)
#print(avion1.__consumo)