import math

def evaluacion():
    if edad < 0:
        raise ValueError("Edad Invalida (Edad menor que 0)")    # Con Raise se elije el error a mostrar
    elif edad < 18:
        return "Eres menor de edad"
    elif edad >= 18:
        return "Eres mayor de edad"
    elif edad >= 65:
        return "Eres jubilado"
    elif edad >= 100:
        return "Eres sigloso"

edad = int(input("Ingrese su edad: "))

print(evaluacion())