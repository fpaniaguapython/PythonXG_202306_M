from time import sleep

PAUSA = 3

def saludar():
    print("Preparando saludo...")
    sleep(PAUSA)
    print("Hola")

def despedir():
    print("Preparando despedida...")
    sleep(PAUSA)
    print("Adios")

def saltar():
    print("Preparando salto...")
    sleep(PAUSA)
    print("Saltando")

def get_saludo():
    return "Hola"

rdo = get_saludo()#Hola
rdo = saludar()#None
rdo = get_saludo#<function get_saludo at 0x000002457C0CAB60>
rdo()

print("Iniciando el gestor de tareas")
lista_tareas = [saludar, saludar, saltar, despedir, saludar, saltar, saltar, saltar, despedir]
while(len(lista_tareas)>0):
    lista_tareas.pop(0)()



