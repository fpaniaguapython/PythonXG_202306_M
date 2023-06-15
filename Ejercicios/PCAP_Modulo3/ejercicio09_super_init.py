class A:
    def __init__(self):
        print("En el init")
        self.a = 1

class B(A):
    def __init__(self) -> None:
        super().__init__()
        #A.__init__(self)#Hay que pasar el sef, porque A no tiene self
        self.b = 2

b = B()