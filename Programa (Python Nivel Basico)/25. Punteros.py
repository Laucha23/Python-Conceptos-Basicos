from io import open

archivo_texto = open("24.1_archivo.txt","r")

# Los archivos arrancan a leerse desde donde ubicado el cursor. Una vez leido todo el archivo, el cursor quedara ubicado en el final

print(archivo_texto.read())

print("\n")

archivo_texto.seek(15)  # Con la funcion .seek() podemos ubicar a nuestro cursor

print(archivo_texto.read(5))   # El numero introducido en el .read() seran los caracteres leidos por el cursor

# ACLARACION: Una vez leido el archivo, si no movemos el cursor, este quedara en el final impidiendo la relectura