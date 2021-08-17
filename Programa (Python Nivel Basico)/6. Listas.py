# Colecciones / Listas

# Las listas, como en la mayoria de lenguajes, arrancan a contar desde el 0, puede contener strings, integer, float u otras listas dentro
# Len sirve para contar los elementos de la lista

"""
lista = ["Lunes" , "Martes" , "Miercoles" , "Jueves" , "Viernes"]
print(len(lista[0:4]))
"""

# .append agrega elementos al final
# .insert cambia el valor de una posicion, en las () primero se coloca la posicion y despues el valor
# .extend agrega varios valores al final de la lista

"""
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.insert(2,4.01)
lista.extend([6, 7, 8])
print(lista)
"""

# .split divide las palabras de una oracion en strings diferentes
# .join agrega los caracteres que elijas a una lista

"""
paises = ["Argentina", "Uruguay", "Paraguay", "Brasil"]
paisesstring = ",".join(paises)
print(paisesstring)

nombrestring = "Me llamo Teodoro"
nombrelista = nombrestring.split()
print(nombrelista)
"""

# Sumatoria de Listas

# la funcion In para las listas define si es true o false si el elemento esta en la lista
# .index define en que posicion se encuentra el elemento, si no esta, tira error
# .count cuenta cuantos valores hay, ya sean repetidos o unicos
# .pop funciona para eliminar elementos dependiendo la posicion
# .remove elimina elementos por valor, en vez de por posicion
# .clear elimina toda la lista
# .sort ordena los elementos de la lista ascendentemente
# .sort(reverse=true) los ordena descendentemente

"""
lista1 = ["Coca", "Pepsi", "Sprite" ]
lista2 = ["Manaos", "Fanta", "Secco"]
lista3 = lista1 + lista2
print("Manaos" in lista3)
print(lista3.index("Manaos"))
print(lista3.count("Secco"))
lista3.pop(3)
lista3.remove(5)
lista3.sort
lista3.sort(reverse=True)
"""