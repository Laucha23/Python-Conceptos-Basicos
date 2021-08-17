# Archivos Externos
# 4 Fases: Creacion, Apertura, Manipulacion y Cierre

from io import open # Biblioteca a importar la funcion Open

# Tendremos que aclarar dos parametros, el nombre y el modo (Lectura, Escritura, Append, y mas)
# Para utilizar el formato de lectura y escritura. Ponemos r+
# Si el archivo a abrir no existe, se crea en la carpeta.


# Usaremos el modo escritura (w de write) 

archivo_texto = open("24.1_archivo.txt", "w")    
frase = "Que lindo que es aprender Python \nEl mejor lenguaje\n"

archivo_texto.write(frase)  # o archivo_texto.write("Que lindo que es aprender Python \nEl mejor lenguaje\n")  

# Para el modo lectura, se realizan los mismos pasos, cambiando el modo (r de read)

archivo_texto = open("24.1_archivo.txt", "r")  
texto = archivo_texto.read()

print(texto)

# Modo Append (a de append)

archivo_texto = open("24.1_archivo.txt", "a")   # Cada vez que cambio el modo de uso, tengo que volver a abrir el archivo
archivo_texto.write("Python > C#")

# Lectura de lineas

print("\n")

archivo_texto = open("24.1_archivo.txt", "r")
lineasTexto = archivo_texto.readlines()         # Lee la lineas y convierte la info en una lista manipulable
print(lineasTexto)

lineasTexto = archivo_texto.close()             # El archivo se cierra al final




