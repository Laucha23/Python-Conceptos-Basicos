# Generadores
# Yield guarda los datos en un objeto iterable, ocupando menos memoria, ya que va guardando los datos de a uno

# Metodo tradicional con Return, crea toda la lista reservando y ocupando mas memoria. 


def generaParesTradicional(limite):

    num = 1
    miLista = []

    while num < limite:
        miLista.append(num*2)
        num += 1
    return miLista


# Metodo con Yield, va creando la lista a medida que se utilizan los items y solo ocupa en memoria,
# el espacio del item utilizado en ese momento.


def generadorDePares(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1

devuelvePares = generadorDePares(10)

for i in devuelvePares:
    print(i)


# Cuando el metodo Yield no se usa, queda en estado de Suspension


def generadorEnSuspension(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1

devuelvePares = generadorEnSuspension(10)

print(next(devuelvePares))  # Next sirve para devolver el siguiente elemento de la Lista

print("Codigo de relleno")

print(next(devuelvePares))

print("Codigo de relleno")

print(next(devuelvePares))
