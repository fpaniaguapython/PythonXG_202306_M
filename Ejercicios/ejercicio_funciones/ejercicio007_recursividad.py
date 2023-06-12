# 4! = 4*3*2*1
# 4! = 4*3!
# 3! = 3*2!
# 2! = 2*1

def factorial(numero):
    if (numero>1):
        resultado = numero * factorial(numero-1)
    else:
        resultado = numero * 1
    return resultado

print(factorial(6))#720
#print(factorial(1000))#24 #Error RecursionError (Stack Overflow)