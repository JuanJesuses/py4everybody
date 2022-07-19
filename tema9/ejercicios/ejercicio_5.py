""" Ejercicio 5: Este programa almacena el nombre del dominio (en vez de la dirección) desde donde fue enviado
    el mensaje en vez de quién envió el mensaje (es decir, la dirección de correo electrónica completa). Al
    final del programa, imprime el contenido de tu diccionario. """

try:
    archivo = open('mbox-short.txt')
except:
    print('No se puede abrir el archivo,', archivo)
    exit()

diccionario = dict()

for linea in archivo:
    linea = linea.rstrip()
    if not linea.startswith('Author:'):
        continue
    palabras = linea.split()
    busca_direccion = palabras[1].split('@')
    direccion = busca_direccion[1]

    if direccion not in diccionario:
        diccionario[direccion] = 1
    else:
        diccionario[direccion] += 1

print(diccionario)
