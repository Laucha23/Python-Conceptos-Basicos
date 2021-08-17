# Ejercicio 1

"""
numero1 = int(input("Ingrese un numero para saber si es par o impar: "))
numero2 = int(input("Ingrese un numero para saber si es par o impar: "))
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos numeros son pares")
elif numero1 %2 != 0 and numero2 % 2 == 0:
    print(f"El numero 1: {numero1}, es impar y el numero 2: {numero2}, es par")
elif numero2 %2 != 0 and numero1 % 2 == 0:
    print(f"El numero 1: {numero1}, es par y el numero 2: {numero2}, es impar")
else:
    print("Ambos numeros son impares")
"""

# Ejercicio 2

"""
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El numero mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El numero mayor es: {num2}")
elif num3 >= num1 and num3 >= num1:
    print(f"El numero mayor es: {num3}")
"""

# Ejercicio 3
# .lower sirve para convertir la letra a minusculas, .upper sirve para convertir la letra a mayuscula
# Sino el filtro no funciona ya que Python es sensible a letras mayusculas/minusculas

"""
letra = input("Ingrese una letra: ").upper()

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("Es una vocal")
else:
    print("No es una vocal")
"""

# Ejercicio 4: Calculadora (4 Operaciones)

"""
num1 = float(input("Ingrese un primer numero: "))
num2 = float(input("Ingrese un segundo numero: "))

operacion = input("Ingrese que operacion le gustaria realizar ingresando su inicial (Suma, Resta, Multiplicacion/Producto y Division): ").upper()
if operacion == "S":
    print(f"La suma es igual a: {num1 + num2}")
elif operacion == "R":
    print(f"La resta es igual a: {num1 - num2}")
elif operacion == "M":
    print(f"la multiplicacion es igual a {num1 * num2}")
elif operacion == "D" or operacion == "P":
    print(f"La division es igual a {num1 / num2:.2f}")
else:
    print("No eligio ninguna operacion seleccionable")
"""

# Ejercicio 5: Cajero Automatico

"""
operacion = input("Ingrese la operacion a realizar, ingresando el nombre de operacion: \n 1. INGRESO \n 2. RETIRO \n 3. MOSTRAR \n 4. SALIR \n \n ").upper()
cajero = 1000

if operacion == "1":
    ingreso = float(input("Escriba el monto a ingresar $ "))
    cajero += ingreso
    print(f"El monto actualizado es de $ {cajero:.2f}")
elif operacion == "2":
    retiro = float(input("Escriba el monto a retirar $ "))
    if retiro > cajero:
        print("No hay suficiente dinero en la cuenta")
    else:
        cajero -= retiro
        print(f"El monto actual es de $ {cajero:.2f}")
elif operacion == "3":
    mostrar = print(f"El saldo en la cuenta es de $ {cajero:.2f}")
elif operacion == "4":
    print("Vuelva pronto")
else:
    ("Ninguna seleccion posible ha sido seleccionada")

"""