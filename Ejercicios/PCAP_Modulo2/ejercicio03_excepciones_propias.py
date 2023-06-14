def sumar(s1: int, s2: int) -> int:
    if not isinstance(s1, int) or not isinstance(s2, int):
        raise TypeError("Los parámetros deben ser enteros")
    resultado = s1 + s2
    return resultado


def dividir(dividendo: float, divisor: float) -> float:
    if divisor == 0.0:
        raise ValueError("El divisor no puede ser 0")
    resultado = dividendo / divisor
    return resultado


try:
    sumar("3", 4)
except TypeError as te:
    print(te)
try:
    dividir(8.0, 0.0)
except ValueError as zde:
    print(zde)