""" Agrega código al programa anterior para determinar quién tiene la mayoría de mensajes en el archivo.
    Después de que todos los datos hayan sido leídos y el diccionario haya sido creado, mira a través
    del diccionario utilizando un bucle máximo (ve Capítulo 5: Bucles máximos y mínimos) para encontrar quién
    tiene la mayoría de mensajes e imprimir cuántos mensajes tiene esa persona.

    Ingresa un nombre de archivo: mbox-short.txt
    cwen@iupui.edu 5
    Ingresa un nombre de archivo: mbox.txt
    zqian@umich.edu 195 """
try:
    archivo = open('mbox.txt')
except:
    print('No se puede abrir el archivo ', archivo)
    exit()

diccionario_correos = dict()
mayor = 0
valor_mayor = 0

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
        for clave in diccionario_correos:
            if diccionario_correos[clave] > mayor:
                mayor = diccionario_correos[clave]

# Solución 1
for valor_mayor in diccionario_correos:
    if diccionario_correos[valor_mayor] == mayor:
        print(valor_mayor, diccionario_correos[valor_mayor])

# Solución 2
"""
lista = list(diccionario_correos.keys())[list(diccionario_correos.values()).index(mayor)]
print(lista, mayor) """

# Solución 3
"""
mayor = max(diccionario_correos, key = diccionario_correos.get)
valor_mayor = diccionario_correos.get(mayor, 0) """