""" Escribe un programa para leer a través de un historial de correos, construye un histograma utilizando un
    diccionario para contar cuántos mensajes han llegado de cada dirección de correo electrónico, e imprime
    el diccionario.

    Ingresa un nombre de archivo: mbox-short.txt


    {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
    'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
    'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
    'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
    'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
    'ray@media.berkeley.edu': 1} """

try:
    archivo = open('mbox-short.txt')
except:
    print('No se puede abrir el archivo ', archivo)
    exit()

diccionario_correos = dict()

for linea in archivo:
    linea = linea.rstrip()
    if linea.startswith('From'):
        if linea.startswith('From:'):
            continue
        palabra = linea.split()
        if palabra[1] not in diccionario_correos:
            diccionario_correos[palabra[1]] = 1
        else:
            diccionario_correos[palabra[1]] += 1

print(diccionario_correos)