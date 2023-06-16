def verdadero():
    print("Verdadero")
    return True

def falso():
    print("Falso")
    return False


#verdadero() and verdadero()#Verdadero - Verdadero
#falso() and verdadero()#Falso
#falso() & verdadero())#Falso - Verdadero

#verdadero() or falso()#Verdadero
#verdadero() | falso()#Verdadero - Falso 

#print(verdadero() or verdadero())#True
print(verdadero() ^ verdadero())#Falso XOR
print(verdadero() ^ falso())#True XOR
print(falso() ^ verdadero())#True XOR