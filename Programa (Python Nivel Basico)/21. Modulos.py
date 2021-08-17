# Modulos

# Pueden ser archivos .py, .pyc (Python Compilado) o .c (CPython)
# Funcionan para organizar y/o reutilizar codigo de manera ordenada (Modularizacion y Reutilizacion)


def sumar(op1, op2):
    return(f"El resultado de la suma es: {op1 + op2}")

def restar(op1, op2):
    return(f"El resultado de la suma es: {op1 - op2}")

def producto(op1, op2):
    return(f"El resultado de la suma es: {op1 * op2}")


# Uso de Modulos

"""

1.  Para utilizar un modulo en otro archivo de codigo, debemos poner alguna de estas opciones

    import Modulos | from Modulos import * | from Modulos import sumar

    El from sirve para elegir el nombre del archivo del modulo a llamar, y el import para seleccionar que importar del modulo.
    Si ponemos *, importaremos todo el modulo, OJO, en muchos casos el modulo puede ser grande y aumentar mucho el tamaño del programa

2.  Las funciones importadas del modulo pueden ser llamadas como una funcion normal ej: sumar()

    print(sumar(7, 6))

    print(producto(8, 8))

"""

