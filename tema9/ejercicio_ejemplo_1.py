""" Ejercicio 1: Descargar una copia del archivo www.py4e.com/code3/words.txt.  Escribe un programa que lee las palabras
    en words.txt y las almacena como claves en un diccionario. No importa qué valores tenga. Luego puedes utilizar
    el operador in como una forma rápida de revisar si una cadena está en el diccionario. """
texto = open('words.txt')
contador = 0
diccionario_palabras = dict()

for linea in texto:
    palabras = linea.split()
    for palabra in palabras:
        diccionario_palabras[palabra] = contador
        # diccionario_palabras[contador] = palabra <-- De esta manera las claves serían los números, no las palabras.
        contador += 1

print(diccionario_palabras)

texto.close()

