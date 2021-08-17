# Operaciones Aritmeticas


# Ejercicio 1

"""
a = float(input("Escriba su numero A: "))
b = float(input("Escriba su numero B: "))

solucion = (((3+5*8)<3 and ((-6/3*4) + 2<2) or (a > b)))
print(solucion)
"""

# Ejercicio 3 (Intercambio de valores entre variables)

"""
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")
a , b = b , a

print(f"El valor de a ahora es {a} y el valor de b ahora es {b}")
"""

# Ejercicio 4 (Mediante el radio, calcular diametro y longitud)

# Import sirve para usar variables con valores predeterminados. En este caso usamos pi 
# El :.2f sirve para indicar cuantos numeros despues de la coma quiero mostrar

"""
import math
radio = float(input("Ingrese el valor del radio de su circunferencia: "))
area = math.pi * radio**2
longitud = (2*math.pi*radio)
 
print(f"El area de la circunferencia es: {area:.2f} y la longitud es: {longitud:.2f}")
"""

# Ejercicio 5 (Pedir el monto a pagar y hacer un descuento del 15%)

"""
import math
precio = float(input("Ingrese el valor del monto a pagar: $"))
descuento = precio * 0.15
preciof = precio - descuento
print(f"El monto a pagar con el descuento aplicado es: $ {preciof:.2f}")
"""