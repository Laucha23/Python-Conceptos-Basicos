# Clases y Objetos

class Coche():
    largoChasis = 250   # Propiedad
    anchoChasis = 100   # Propiedad
    ruedas = 4          # Propiedad
    enMarcha = False    # Propiedad Estado

    def arrancar(self):     # Comportamiento
        self.enMarcha = True

    def estado(self):       # Comportamiento
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

miCoche = Coche()       # Instanciar una clase

print(f"El largo del coche es {miCoche.largoChasis}")
print(f"El ancho del coche es {miCoche.anchoChasis}")

miCoche.arrancar()

print(miCoche.estado())