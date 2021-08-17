# Bucle For

for i in [1,2,3,4,5,6]:     # la funcion For, hace todo el recorrido con un auxiliar (en este caso, i) hasta que recorre todo
    print(f"Hola: {i}")


coleccion = ["a","b","c","d","e"]
for i in coleccion:
    print(f"Hola: {i}")


coleccion = {"Fernando":23,"Tomas":40,"Luciana":90}
for valor,llave in coleccion.items():
    print(f"El nombre y la edad es: {valor} , {llave}")


coleccion = "Python"
for i in coleccion:
    print(f"{i}",end = " ")


# Bucle For con Rango

for i in range (50):
    print(f"Contador hasta {i}")

for i in range(4,25):
    print(f"Contador de 4 hasta 24: {i}")

