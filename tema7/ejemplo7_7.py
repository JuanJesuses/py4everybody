""" ¿Qué tal si nuestro usuario escribe algo que no es un nombre de archivo?
Ahora que vemos el defecto en el programa, podemos arreglarlo de forma elegante
utilizando la estructura try/except.
Necesitamos asumir que la llamada a open
podría fallar y agregar código de recuperación para ese fallo, así: """

narchivo = input('Introduce un nombre de archivo: ')
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