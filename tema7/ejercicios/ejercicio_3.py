""" Ejercicio 3: Algunas veces cuando los programadores se aburren o
quieren divertirse un poco, agregan un inofensivo Huevo de Pascua
a su programa. Modifica el programa que pregunta al usuario por el
nombre de archivo para que imprima un mensaje divertido cuando el
usuario escriba “na na boo boo” como nombre de archivo. El programa
debería funcionar normalmente para cualquier archivo que exista o no
exista. Aquí está un ejemplo de la ejecución del programa:

python huevo.py
Ingresa un nombre de archivo: mbox.txt
Hay 1797 líneas subject en mbox.txt

python huevo.py
Ingresa un nombre de archivo: inexistente.tyxt
El archivo no puede ser abierto: inexistente.tyxt
python huevo.py

Ingresa un nombre de archivo: na na boo boo
NA NA BOO BOO PARA TI - Te he atrapado! """

"""import os

for f in os.listdir('/home/john/eclipse-workspace/ejercicios_libro/tema7'):
    print(f)"""

narchivo = input('Introduce un nombre de archivo: ')
if narchivo == 'na na boo boo':
    print('NA NA BOO BOO PARA TI - Te he atrapado!')
    exit()
try:
    man_a = open(narchivo)
except:
    print('No se puede abrir el archivo:', narchivo)
    exit()
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay ', contador, ' líneas de asunto (subject) en', narchivo)



