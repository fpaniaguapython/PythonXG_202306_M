class Almacen:
    def __init__(self) -> None:
        self.productos = [('Colchón',10),('Mesa',0),('Lámpara',15)]

    def __iter__(self):
        self.contador = -1
        return self #Almacen se está proporcionando como iterador
    
    def __next__(self):
        self.contador+=1
        if self.contador==len(self.productos):
            raise StopIteration
        return self.productos[self.contador]

almacen1 = Almacen()

for mueble in almacen1:
    print(mueble)