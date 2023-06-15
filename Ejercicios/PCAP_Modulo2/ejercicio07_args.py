
try:
    x = 7 / 0
except ArithmeticError as ae:
    print(ae.args)