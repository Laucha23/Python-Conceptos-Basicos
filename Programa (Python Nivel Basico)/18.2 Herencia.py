# Herencia y MultiHerencia
# Sobreescritura de metodos

class Vehiculos():
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True 

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}")


class Moto(Vehiculos):  # Defino una nueva subclase de Vehiculos. Por ende, obtiene sus propiedades
    haciendowilly = ""

    def willy(self):
        self.haciendowilly =  "Voy haciendo la Willy"
        self.enmarcha = True

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}\n{self.haciendowilly} ")

class VehiculosElectricos():
    def __init__(self):
        self.energia = 100

    def cargarEnergia(self):

        self.cargando = True

class BiciElectrica(Vehiculos, VehiculosElectricos):
    pass
    """
    Para pasarle los parametros a un objeto en una herencia multiple, hay que poner primero en los parametros,
    a la clase de los parametros a copiar
    """

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}\nEnergia: {self.energia} ")


moto1 = Moto("Toyota", "1500")  # Utilizo los mismo parametros que puse en Vehiculo (Marca, Modelo)
moto1.willy()
moto1.estado() # El metodo estado de Moto sobrescribe el metodo estado de Vehiculo (Clase Padre)
print("\n")
bici1 = BiciElectrica("Yamaha", "HCD50")
bici1.energia = 70
bici1.estado()