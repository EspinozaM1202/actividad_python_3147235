# operaciones.py

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(a, b):
    return a ** b

def division_entera(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a // b
