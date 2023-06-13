print("Modulo 1")

nombre_m1="Nombre m1"#Es visible
_nombre_m1="Nombre m2"#Está oculta?
__nombre_m1="Nombre m3"#Está oculta

def f1_1():#Es visible
    print("f1_1")

def _f1_2():#Es visible
    print("f1_2")

def __f1_3():#Está oculta
    print("f1_3")

if __name__=='__main__':
    pass

