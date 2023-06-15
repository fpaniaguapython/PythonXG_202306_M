class Alumno:
    def __init__(self, saldo_inicial) -> None:
        self.__saldo = saldo_inicial

    #Métodos de acceso - getters y setters
    def get_saldo(self) -> int:
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    def obtener_dinero(self, dinero_solicitado):
        if (dinero_solicitado)>10:
            raise ValueError("No puedes pedir más de 10€")
        self.set_saldo(self.get_saldo() - dinero_solicitado)
        return dinero_solicitado
    
    #Método oculto o 'privado' (está renombrado a _Alumno__recalcular_saldo)
    def __recalcular_saldo(self):
        pass


lorena = Alumno(98)
#lorena.__saldo-=50 #Generar un error porque __ oculta el atributo
print("Saldo:", lorena.get_saldo())
lorena.set_saldo(51)
print("Saldo:", lorena.get_saldo())







#Anexo: El atributo __saldo se ha convertido en _Alumno__saldo
lorena._Alumno__saldo-=30 
