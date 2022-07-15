""" Definitivamente no queremos tener que editar nuestro código Python cada vez
que queremos procesar un archivo diferente. Sería más útil pedir al usuario que
introduzca el nombre del archivo cada vez que el programa se ejecuta, de modo
que pueda usar nuestro programa en diferentes archivos sin tener que cambiar el
código.
Esto es sencillo de hacer leyendo el nombre de archivo del usuario utilizando input
como se muestra a continuación: """

narchivo = input('Introduce un nombre de archivo: ')
man_a = open(narchivo)
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay', contador, ' líneas de asunto (subject) en ', narchivo)