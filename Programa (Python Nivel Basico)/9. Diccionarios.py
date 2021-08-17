# Diccionarios

"""
diccionario = {"azul":"blue","rojo":"red","verde":"green"}

diccionario["amarillo"] = "yellow"
del(diccionario["verde"])
print(diccionario)
print(diccionario["azul"])


diccionario1 = {"Horacio":[60,1.73],"Jose":[26,1.9],"Mariela":[45,1.6]}
print(diccionario1)
print(diccionario1["Mariela"])
"""

# Diccionarios

# .get() consigue un valor con la llave. con la coma se puede poner una excepcion por si no hay un valor asignado a esa llave
# In sirve para comprobar si un valor o llave esta en el diccionario, con respuesta booleana
# .keys() y .values() sirve para mostrar las llaves/valores del diccionario.
# .items muestra las keys y valores a la par
# .clear limpia el diccionario

"""
equipo = {10:"Dybala",11:"Douglas",7:"Ronaldo"}
print(equipo.get(10, "No existe"))
print(equipo.get(5, "No existe"))

print(10 in equipo)
print(13 in equipo)

print(equipo.keys())
print(equipo.values())
print(equipo.items())
equipo.clear()
"""