# Yield From
# Sirve para recorrer sub-elementos, evitando usar otro For. Ademas Sirve para armar arrays

def funcionCiudades(*ciudades): # el * sirve para avisarle a Python que va a recibir un nro indeterminado de elementos y en formato Tupla
    for elemento in ciudades:
            yield from elemento # Yield From selecciona sub-elementos del elemento recorrido

ciudades_devueltas = funcionCiudades("Madrid", "BsAs", "Roma", "Montevideo")

print(next(ciudades_devueltas)) # Next sirve para devolver el siguiente elemento de la Lista, Tupla, Array, etc.
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
