# Herencia

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
    pass

moto1 = Moto("Toyota", "1500")
moto1.estado()




