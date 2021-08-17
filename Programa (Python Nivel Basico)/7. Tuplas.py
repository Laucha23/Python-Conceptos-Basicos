# Tuplas (Listas inmodificables, que solo se pueden leer, van con () ). Son mas rapidas y pesan menos

# Las Tuplas pueden pasar a ser listas y viceversa, con copías de estas

tupla = ("Messi", "Maradona", "Pele" )
lista = list(tupla)
tupla = tuple(lista)

print(tupla)
