""" La salida parece correcta puesto que las líneas que estamos buscando son aquellas
que comienzan con “From:”, pero ¿por qué estamos viendo las líneas vacías extras?
Esto es debido al carácter invisible salto de línea. Cada una de las líneas leídas
termina con un salto de línea, así que la sentencia print imprime la cadena alma-
cenada en la variable line, la cual incluye ese salto de línea, y después print agrega
otro salto de línea, resultando en el efecto de doble salto de línea que observamos. """

man_a = open('mbox-short.txt')
contador = 0
for linea in man_a:
    if linea.startswith('From:'):
        contador = contador + 1
        print(linea)
print(contador)

""" Podemos usar troceado de líneas para imprimir todos los caracteres excepto el
último, pero una forma más sencilla es usar el método rstrip, el cual elimina los
espacios en blanco del lado derecho de una cadena, tal como: """

man_a = open('mbox-short.txt')
for linea in man_a:
    linea = linea.rstrip() #rstrip() elimina los espacios en blanco del lado derecho de una cadena
    if linea.startswith('From:'):
        print(linea)

""" A medida que tus programas de procesamiento de archivos se vuelven más compli-
cados, quizá quieras estructurar tus bucles de búsqueda utilizando continue. La
idea básica de un bucle de búsqueda es que estás buscando líneas “interesantes” e
ignorando líneas “no interesantes”. Y cuando encontramos una línea interesante,
hacemos algo con ella.

Podemos estructurar el bucle para seguir el patrón de ignorar las líneas no intere-
santes así: """

man_a = open('mbox-short.txt')
for linea in man_a:
    linea = linea.rstrip()
    # Ignoramos las líneas que no nos interesan
    if not linea.startswith('From:'):
        continue
    # Procesamos la línea que nos interesa
    print(linea)

""" Podemos usar el método de cadenas find para simular la función de búsqueda de
un editor de texto, que encuentra las líneas donde aparece la cadena de búsqueda
en alguna parte. Puesto que find busca cualquier ocurrencia de una cadena dentro
de otra y devuelve la posición de esa cadena o -1 si la cadena no fue encontrada,
podemos escribir el siguiente bucle para mostrar las líneas que contienen la ca-
dena “@uct.ac.za” (es decir, los que vienen de la Universidad de Cape Town en
Sudáfrica): """

man_a = open('mbox-short.txt')
for linea in man_a:
    linea = linea.rstrip()
    if linea.find('@uct.ac.za') == -1:
        continue
    print(linea)







