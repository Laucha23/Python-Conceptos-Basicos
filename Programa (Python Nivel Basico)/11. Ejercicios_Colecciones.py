# Ejercicio 1

"""
# Con el comando set transformo la lista en conjunto, como en los conjuntos no pueden haber dos valores iguales, los elimina y con el list vuelve a ser una lista
# Forma corta
lista = [1,2,3,4,5,5,5,2,7,8]
lista = list(set(lista))
print(lista)

# Forma Larga
lista = [1,2,3,4,5,5,5,2,7,8]
conjunto = (set(lista))
lista = list(conjunto)
print = (lista)
"""

# Ejercicio 2

"""
lista1 = [1,2,3,4,5,5,5,7,1,1]
lista2 = [6,6,6,8,1,2,3,0,71]
a = set(lista1)
b = set(lista2)

union = list(a | b)
l1 = list(a - b)
l2 = list(b - a)
cruce = list(a & b)

print(f"Todos los elementos son: { union } ")
print(f"los elementos que solamente aparecen en la lista 1 son: { l1 } ")
print(f"los elementos que solamente aparecen en la lista 2 son: { l2 } ")
print(f"La interseccion es: {cruce}")
"""

# Ejercicio 3

"""
personajes = []

per1 = {"Nombre":"Aragorn" , "Clase":"Guerrero" , "Lugar":"Dunadan del Norte"}
per2 = {"Nombre":"Gandalf" , "Clase":"Mago" , "Lugar":"Istar"}
per3 = {"Nombre":"Legolas" , "Clase":"Arquero" , "Lugar":"Elfo Sindar"}

personajes.append(per1)
personajes.append(per2)
personajes.append(per3)

print(personajes)
"""