""" Escribir un programa que clasifica cada mensaje de correo dependiendo del día de la semana en que se recibió.
    Para hacer esto busca las líneas que comienzan con “From”, después busca por la tercer palabra y mantén un contador
    para cada uno de los días de la semana. Al final del programa imprime los contenidos de tu diccionario (el orden
    no importa).

    Línea de ejemplo:
    From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

    Ejemplo de ejecución:
    python dow.py
    Ingresa un nombre de archivo: mbox-short.txt
    {'Fri': 20, 'Thu': 6, 'Sat': 1} """
import string

try:
    archivo = open('mbox-short.txt')
except:
    print('No se puede abrir el archivo ', archivo)
    exit()

diccionario_dias = dict()
contador = 1
for linea in archivo:
    if linea.startswith('From'):
        if linea.startswith('From:'):
            continue
        linea = linea.split()
        if linea[2] not in diccionario_dias:
            diccionario_dias[linea[2]] = 1
        else:
            diccionario_dias[linea[2]] += 1
print(diccionario_dias)