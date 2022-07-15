import string

""" En el ejemplo anterior utilizando el archivo romeo.txt, hicimos el archivo tan simple
    como fue posible removiendo los signos de puntuación a mano. El text real tiene
    muchos signos de puntuación, como se muestra abajo. 
    
    But, soft! what light through yonder window breaks?
    It is the east, and Juliet is the sun.
    Arise, fair sun, and kill the envious moon,
    Who is already sick and pale with grief,
    
    Puesto que la función split en Python busca espacios y trata las palabras como
    piezas separadas por esos espacios, trataríamos a las palabras “soft!” y “soft” como
    diferentes palabras y crearíamos una entrada independiente para cada palabra en
    el diccionario.
    Además, como el archivo tiene letras mayúsculas, trataríamos “who” y “Who”
    como diferentes palabras con diferentes contadores.
    Podemos resolver ambos problemas utilizando los métodos de cadenas lower,
    punctuation, y translate. El método translate es el más sutil de los métodos.
    Aquí esta la documentación para translate:
    
    line.translate(str.maketrans(fromstr, tostr, deletestr))
    Reemplaza los caracteres en fromstr con el caracter en la misma posición en tostr
    y elimina todos los caracteres que están en deletestr. Los parámetros fromstr y
    tostr pueden ser cadenas vacías y el parámetro deletestr es opcional. """

fname = input('Introduce el nombre del archivo: ')
try:
    fhand = open(fname)
except:
    print('El archivo no se puede abrir: ', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)