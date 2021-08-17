# Constructores, Encapsulamiento e Instancias

class Coche():
    # Es indispensable usar el self. dentro de un constructor/comportamiento
    def __init__(self): # Constructor

        self.largoChasis = 250   # Propiedad
        self.anchoChasis = 100   # Propiedad
        self.__ruedas = 4        # Propiedad Encapsulada ( __ Sirve para encapsular)
        self.enMarcha = False    # Propiedad Estado

    def arrancar(self, arrancamos):     # Comportamiento
        self.enMarcha = arrancamos      # Si llamamos a Arrancar, va a activar enMarcha que esta en el init
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):       # Comportamiento
        return(f"El coche tiene: {self.__ruedas} ruedas. Un ancho de {self.anchoChasis}. y un largo de {self.largoChasis} ")

miCoche = Coche()       # Instanciar una clase

print(miCoche.arrancar(True))
print(miCoche.estado())

print("Segundo Objeto")

miCoche2 = Coche()       # Instanciar una clase

print(miCoche2.arrancar(False))
miCoche2.__ruedas = 5   # Al estar encapsulada la propiedad, no va a sufrir cambios por mas que lo intentes
print(miCoche2.estado())