# Rebanado de cadenas. El rebanado de cadenas, también funciona en listas:

t = ['a', 'b', 'c', 'd', 'e', 'f']

# Ejemplo_1

print(t[1:3])

# Ejemplo_2

print(t[:4])

# Ejemplo_3

print(t[3:])

""" Si omites el primer índice, el rebanado comienza desde el inicio de la lista. Si
omites el segundo, el rebanado se va hasta el final. Así que si omites ambos, el
rebanado es una copia de la lista completa. """

print(t[:])

""" Como las listas son mutables, a veces es útil hacer una copia antes de hacer opera-
ciones que doblan, pegan, o cortan listas. """

""" Un operador de rebanado al lado izquierdo de una asignación puede actualizar
múltiples elementos: """

t2 = t

print(t2)

t[1:3] = ['x', 'y']

print(t)







