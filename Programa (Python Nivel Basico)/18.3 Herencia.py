# Herencia
# Funciones Super() y IsIstance()

# Super() sirve para tomar las propiedades de un constructor padre
# IsIstance sirve para chequear si un objeto pertenece a una clase y devuelve True o False. Ejemplo: Antonio con Persona

class Persona():
    def __init__(self, nombre, edad, residencia):
        
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):

        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nResidencia: {self.residencia}")

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) 
        # La funcion Super(), llama al constructor de la Clase Padre, en este caso, Clase Persona
        # Con esto tomamos las propiedades del constructor de Persona

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        print(super().descripcion())
        print(f"Salario: {self.salario}\nAntiguedad: {self.antiguedad}")
        

antonio = Empleado(1500, "15 años", "Antonio", 55, "BsAs")
antonio.descripcion()

print (isinstance(antonio, Empleado))
