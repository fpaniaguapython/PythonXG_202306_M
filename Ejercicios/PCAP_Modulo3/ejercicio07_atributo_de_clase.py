class Humano:
    #Atributos de clase
    #Son compartidos por todas las instancias
    #Se referencian como Humano.esperanza_vida
    esperanza_vida = 88
    def __init__(self, nombre, fecha_nacimiento) -> None:
        #Atributos de instancia o de objeto
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento 
    def calcular_vida_restante(self, anho_actual):
        numero_anhos = anho_actual - self.fecha_nacimiento
        vida_restante = Humano.esperanza_vida - numero_anhos
        return vida_restante

hombre1 = Humano("Fernando",1971)
mujer1 = Humano("Sonia",1978)

print(hombre1.nombre)
print(mujer1.fecha_nacimiento)
print(Humano.esperanza_vida)
print(hombre1.calcular_vida_restante(2023))
Humano.esperanza_vida = 90
print(hombre1.calcular_vida_restante(2023))

print(hombre1.__dict__)#Aquí no se muestra el atributo de clase
print(Humano.__dict__)#Aquí sí, pero no se muestran los de instancia

#Uso de hasattr
if hasattr(hombre1, 'fecha_nacimiento'):
    print(hombre1.fecha_nacimiento)
