# Recorriendo una lista
""" La forma más común de recorrer los elementos de una lista es con un bucle for.
La sintaxis es la misma que para las cadenas: """

quesos = ['Chédar', 'Edam', 'Gouda']

for queso in quesos:
    print(queso)

""" Esto funciona bien si solamente necesitas leer los elementos de la lista. Pero si
quieres escribir o actualizar los elementos, necesitas los índices. Una forma común
de hacer eso es combinando las funciones range y len: """

numeros = [25, 56, 78, 903, 12, 43, 5, 1654]

for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2

"""
for i in numeros:
    numeros[i] = numeros[i] * 2 """ # Esto no funciona

print(numeros)

""" Este bucle recorre la lista y actualiza cada elemento. len regresa el número de
elementos en una lista. range regresa una lista de índices desde 0 hasta n − 1,
donde n es la longitud de la lista. Cada vez que pasa a través del recorrido, i
obtiene el índice del siguiente elemento. La sentencia de asignación dentro del
bucle utiliza i para leer el valor original del elemento y asignar un nuevo valor. """








