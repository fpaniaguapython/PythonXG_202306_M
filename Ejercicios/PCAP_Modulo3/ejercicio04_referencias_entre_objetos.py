class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.relacion = None

    def saludar(self, otro):
        print(f'Hola, soy {self.nombre} y te saludo {otro}')

ramon = Persona("Ramón")
alexander = Persona("Alexander")
ramon.relacion = alexander
ramon.relacion.saludar('Jero')


#Los objetos se pasan por referencia
#--> Lo que se modifique dentro de la función/método se modifica fuera
def funcion1(persona):
    persona.nombre*=2

funcion1(ramon)
print(ramon.nombre)

