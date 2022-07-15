""" Para escribir en un archivo, tienes que abrirlo en modo “w” (de write, escritura)
como segundo parámetro: """
fsal = open('salida.txt', 'w')
print(fsal) 

""" Si el archivo ya existía previamente, abrirlo en modo de escritura causará que se
borre todo el contenido del archivo, así que ¡ten cuidado! Si el archivo no existe,
un nuevo archivo es creado. 
El método write del manejador de archivos escribe datos dentro del archivo, de-
volviendo el número de caracteres escritos. El modo de escritura por defecto es
texto para escribir (y leer) cadenas."""

linea1 = "Aquí está el zarzo, \n"

print(fsal.write(linea1))

""" El manejador de archivo mantiene un seguimiento de dónde está, así que si llamas
a write de nuevo, éste agrega los nuevos datos al final.
Debemos asegurarnos de gestionar los finales de las líneas conforme vamos escribi-
endo en el archivo, insertando explícitamente el carácter de salto de línea cuando
queremos finalizar una línea. La sentencia print agrega un salto de línea automáti-
camente, pero el método write no lo agrega de forma automática. """

linea2 = 'el símbolo de nuestra tierra.\n'
print(fsal.write(linea2))
fsal.close()