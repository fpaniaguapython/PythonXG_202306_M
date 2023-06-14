#s1 y s2 deben ser pares
def sumar_pares(s1 : int, s2: int):
    assert(s1%2==0)
    assert(s2%2==0)
    return s1 + s2

#resultado = sumar_pares(3,4)
resultado = sumar_pares(6,4)
print(resultado)