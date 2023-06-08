#break - Forzar la salida de un bucle
#continue - Cancelar la iteracción

equipos = ["Celta de Vigo", "Deportivo de la Coruña", "Compostela"]

#Reglas - Deben tener la letra 'o', la letra 'a', la letra 'ñ'
for equipo in equipos:
    contador=0
    print("FASE 1")
    if 'ñ' in equipo:
        contador+=1
    else:
        continue #Finaliza la iteracción en la que se encuentra
    print("FASE 2")
    if 'o' in equipo:
        contador+=1
    print("FASE 3")
    if 'a' in equipo:
        contador+=1
    
    if contador==3:
        print(equipo,"OK")
        break #Salimos del bucle porque hemos encontrado lo que queríamos
    else:
        print(equipo,"KO")
