import random

#1. Pedir al usuario un número
#2. Si acierta el número secreto --> Es un adivino. Fin de la ejecución.
#3. Si no acierta el número secreto --> Volvemos a pedirle otro número.
#4. El 'adivino' va a tener un número máximo de intentos
NUMERO_MAX_INTENTOS = 3
numero_intentos=0
numero_secreto = random.randint(1,9)
print(numero_secreto)
numero_candidato = -1
while numero_candidato!=numero_secreto and numero_intentos<NUMERO_MAX_INTENTOS:
    numero_candidato = int(input("Introduce el número candidato:"))
    numero_intentos+=1
    if (numero_candidato==numero_secreto):
        print("Eres un adivino")
    else:
        if numero_intentos<NUMERO_MAX_INTENTOS:
            print("No has acertado. Prueba de nuevo...")
        else:
            print("Eres un fraude")
