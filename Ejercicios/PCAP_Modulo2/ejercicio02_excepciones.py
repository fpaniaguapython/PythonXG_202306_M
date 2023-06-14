lista = ['a','b','c']

def dividir(dividendo, divisor):
    resultado = dividendo/divisor
    return resultado

#except genérico
try:
    resultado = dividir(10,0)
    print("Resultado:",resultado)
except:
    print("Except: Ha ocurrido un error")

#except genérico con else (opcional) y finally (opcional)
try:
    resultado = dividir(10,0)
    print("Resultado:",resultado)
except:
    print("Except: Ha ocurrido un error")
else:
    print("Else: Se ejecuta cuando no ha ocurrido una excepción")
finally:
    print("Finally: Siempre después del bloque-try-except")

#except con captura de tipo de error
try:
    resultado = dividir(10,0)
    print("Resultado:",resultado)
except ZeroDivisionError:
    print("Except: No se puede dividir entre 0")

#except con captura de tipo de error y obtener el objeto que tiene el error
try:
    resultado = dividir(10,0)
    print("Resultado:",resultado)
except ZeroDivisionError as zde:
    print("Except: No se puede dividir entre 0:", zde)


#except con captura de dos tipos de error diferentes
try:
    lista[10]
    resultado = dividir(10,0)
    print("Resultado:",resultado)
except ZeroDivisionError:
    print("Except: No se puede dividir entre 0")
except IndexError:
    print("Except: Acceso a un índice inexistente")


#except con captura de dos tipos de error diferentes
#más gestión genérica de varios niveles
try:
    lista[10]
    resultado = dividir(10,0)
    print("Resultado:",resultado)
except ZeroDivisionError:
    print("Except: No se puede dividir entre 0")
except IndexError:
    print("Except: Acceso a un índice inexistente")
except ArithmeticError:
    pass
except Exception:
    pass
except BaseException:
    pass

#except con captura de dos tipos de error diferentes
#más gestión genérica
try:
    lista[10]
    resultado = dividir(10,0)
    print("Resultado:",resultado)
except ZeroDivisionError:
    print("Except: No se puede dividir entre 0")
except IndexError:
    print("Except: Acceso a un índice inexistente")
except BaseException:#Tratamiento genérico para el resto de errores
    pass


#except con captura de dos tipos de error diferentes
#en un único except
try:
    lista[2]
    resultado = dividir(10,0)
    print("Resultado:",resultado)
except (ZeroDivisionError, IndexError) as fallo:
    print("Except: No se puede dividir entre 0 o ha ocurrido un error índice:",fallo)
