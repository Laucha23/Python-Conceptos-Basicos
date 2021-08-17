# Continue & Pass

# Continue
# Una vez activado, salta la vuelta actual en el For, pasando a la siguiente.

"""
for letra in "Python":

    if letra == "h":
        continue

    print(f"Viendo la letra: {letra}")
"""

"""
nombre = "Aprendiendo Python"

contador = 0

for i in nombre:
    if i == " ":
        continue
    else:
        contador += 1

print(contador)
"""

# Pass
# Una vez activado, devuelve un valor 'Null' (No muy utilizado en Python)

"""
mail = input("Ingrese su mail: ")
contador = 0

for i in mail:

    if i == "@":
        contador += 1
        arroba = True

    elif contador >= 1:
        pass # Hace nula la cadena de If / Elif, pasando al Else del For

else:
    arroba = False

print(arroba)
""" 
