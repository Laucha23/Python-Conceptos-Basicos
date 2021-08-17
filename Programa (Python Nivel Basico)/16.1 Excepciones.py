# Excepciones
# Captura de Excepcion

# Try: el programa "Intenta" desarollar la funcion
# Except: De no ser posible el intento, se ejecuta la excepcion. Esta puede ser general o especifica (Ej: ZeroDivisionError)
# Finally: Ocurra lo que ocurra, siempre se va a ejecutar al final. Con o sin excepts

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def producto(num1,num2):
    return num1*num2

def division(num1,num2):
    try:                    # El programa intentara realizar la accion, de no ser asi
        return num1/num2
        
    # Si no ponemos ninguna excepcion particular en Except, funcionara una general para todas las excepciones

    except ZeroDivisionError:   # Analizara entre las excepciones, si coincide, procesara lo incluido en la excepcion
        print("No se puede dividir con 0")
        return "Error"

while True:
    try:
        numero1 = int(input("Ingrese el primer numero: "))
        numero2 = int(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print("\nError en la introduccion de valores")
    finally:
        print("Intento terminado")

operacion = input("Introduzca el nro de operacion a realizar\n 1. Suma\n 2. Resta\n 3. Producto\n 4. Division\n")

if operacion == "1":
    print(suma(numero1,numero2))
if operacion == "2":
    print(resta(numero1,numero2))
if operacion == "3":
    print(producto(numero1,numero2))
if operacion == "4":
    print(division(numero1,numero2))