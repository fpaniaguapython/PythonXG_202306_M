class NoTieneArrobaError(ValueError):
    pass

def validar(email):
    if '@' not in email:
        raise NoTieneArrobaError("No tiene @")
    

email = "fernando.paniagua#gmail.com"
try:
    validar(email)
except NoTieneArrobaError as ntae:
    print(ntae)
    print(ntae.args)