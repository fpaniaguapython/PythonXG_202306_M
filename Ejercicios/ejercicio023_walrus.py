print(x := 10) #Asigna y después hace el print de x

numero_secreto = 3

while (numero_candidato := int(input("Número:")) != numero_secreto):
    print("Error")
else:
    print("OK")
