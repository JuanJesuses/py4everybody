""" Normalmente cuando estamos leyendo un archivo queremos hacer algo con las
líneas que no sea solamente imprimir las líneas como son. Frecuentemente quere-
mos encontrar las “líneas interesantes” y después analizar la línea para encontrar
alguna “parte interesante” en la línea. ¿Qué tal si quisiéramos imprimir el día de
la semana de las líneas que comienzan con “From”?

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 """

""" El método split es muy efectivo cuando nos encontramos este tipo de problemas.
Podemos escribir un pequeño programa que busca líneas donde la línea comienza
con “From”, split (dividir) esas líneas, y finalmente imprimir la tercer palabra de
la línea: """

man_a = open('mbox-short.txt')
for linea in man_a:
    linea = linea.rstrip() # eliminamos los espacios en blanco con rstrip()
    if not linea.startswith('From '):
        continue
    palabras = linea.split() # separamos la linea interesante en una lista de cadenas
    print(palabras[2])  