man_archivo = open('mbox-short.txt')
print(man_archivo)
contador = 0
for linea in man_archivo:
    contador = contador + 1
print('Contador de líneas: ', contador)

""" Si sabes que el archivo es relativamente pequeño comparado al tamaño de tu memo-
ria principal, puedes leer el archivo completo en una sola cadena utilizando el
método read en el manejador de archivos. """

""" En este ejemplo, el contenido completo (todos los 94626 caracteres) del archivo
mbox-short.txt son leídos directamente en la variable inp. Utilizamos el troceado de
cadenas para imprimir los primeros 20 caracteres de la cadena de datos almacenada
en inp. """

manejador_archivo = open('mbox-short.txt')
inp = manejador_archivo.read()
print(len(inp))
print(inp[:20])

""" Cuando el archivo es leído de esta forma, todos los caracteres incluyendo los saltos
de línea son una cadena gigante en la variable inp. Es una buena idea almacenar
la salida de read como una variable porque cada llamada a read vacía el contenido
por completo: """

manejador = open('mbox-short.txt')
print(len(manejador.read()))
print(len(manejador.read()))