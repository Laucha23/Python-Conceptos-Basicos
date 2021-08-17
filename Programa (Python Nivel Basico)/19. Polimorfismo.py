# Polimorfismo

# Funcion adaptable a las circunstancias. Por mas que tengan el mismo nombre, Python analiza todos y usa el correcto

class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")   # Comportamiento

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")  # Comportamiento

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas") # Comportamiento


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)



