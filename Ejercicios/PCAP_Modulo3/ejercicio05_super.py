class Vehiculo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def arrancar(self):
        print(f'Soy Vehiculo {self.nombre} y estoy arrancando')
    def mover(self):
        print(f'Soy Vehiculo {self.nombre} y me estoy moviendo')

class VehiculoTerrestre(Vehiculo):
    def __init__(self, nombre, numero_ruedas) -> None:
        super().__init__(nombre)
        self.numero_ruedas = numero_ruedas

    def rodar(self):
        print(f'Soy VehiculoTerrestre {self.nombre} y estoy rodando')
    def mover(self):
        super().mover()#Llamando al mover de la clase base inmediatamente superior
        print(f'Soy VehiculoTerrestre {self.nombre} y me estoy moviendo')


automovil = VehiculoTerrestre("Panda",4)

#automovil es instancia de VehiculoTerrestre y de Vehiculo.

#POLIMORFISMO
print(isinstance(automovil, VehiculoTerrestre))#True
print(isinstance(automovil, Vehiculo))#True

#SOBREESCRITURA DE MÉTODOS
automovil.mover()

