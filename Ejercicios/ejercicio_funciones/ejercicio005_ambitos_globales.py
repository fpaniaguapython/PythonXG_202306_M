def hacer():
    global x #Utiliza la variable x del ámbito global
    x = 15
    print(x)#15

    global y #Definiendo la variable x como global
    y = 5
    
x = 10
hacer()
print(x)#15
print(y)