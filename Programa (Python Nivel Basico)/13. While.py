# Bucle While infinito y Bucle While definido

import math
numero = int(input("Digite un numero: "))

while numero < 0:   # Mientras la condicion se cumpla, se seguira ejecutando lo que este dentro de la funcion
    print("Error, no ingreso un numero positivo")
    numero = int(input("Digite un numero: "))
    
print(f"\nLa raiz cuadrada del numero {numero} es {(math.sqrt(numero)):.2f}")


i = 0
while i < 10:
    print("buenas")
    i += 1

i = 0
while i < 10:
    print(i)
    i += 1

