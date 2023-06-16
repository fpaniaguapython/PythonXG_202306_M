class A:
    A=1

    def __init__(self) -> None:
        self.nombre="MSI"

ob = A()

print(hasattr(A,'A'))#True, porque 'A' es un atributo de clase de A
print(hasattr(A,'nombre'))#False, porque nombre es un atributo de instancia
print(hasattr(ob,'A'))#True, porque los objetos ven los atributos de clase
print(hasattr(ob,'nombre'))#True, porque los objetos ven sus atributos de instancia
