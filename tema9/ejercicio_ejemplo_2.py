""" Vamos a escribir un programa de Python para leer a través de las líneas del archivo, dividiendo cada línea en una
    lista de palabras, y después iterando a través de cada una de las palabras en la línea y contando cada palabra
    utilizando un diccionario. """
fname = input('Introduce el nombre del archivo: ')
try:
    fhand = open(fname)
except:
    print('No se puede abrir el archivo: ', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)