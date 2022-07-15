""" Cuando estás leyendo y escribiendo archivos, puedes tener problemas con los es-
pacios en blanco. Esos errores pueden ser difíciles de depurar debido a que los
espacios, tabuladores, y saltos de línea son invisibles normalmente: """

s = '1 2\t 3\n 4'
print(s)

""" La función nativa repr recibe cualquier objeto como argumento
y devuelve una representación del objeto como una cadena. En el caso de las
cadenas, representa los espacios en blanco con secuencias de barras invertidas: 
Esto puede ser útil para depurar. """

print(repr(s))

""" Otro problema que podrías tener es que diferentes sistemas usan diferentes carac-
teres para indicar el final de una línea. Algunos sistemas usan un salto de línea,
representado como \n. Otros usan un carácter de retorno, representado con \r.
Otros usan ambos. Si mueves archivos entre diferentes sistemas, esas inconsisten-
cias podrían causarte problemas. """