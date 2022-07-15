""" Hay varias formas de eliminar elementos de una lista. Si sabes el índice del elemento
que quieres, puedes usar pop: """

t = ['a', 'b', 'c']
t2 = t.copy() # esto si hace una copia, t2 = t sólo apunta al objeto t y si modificas t o t2 se modifican ambos
t2 = t # esto apunta a t pero no crea una copia de t en t2
# t2 = ['a', 'b', 'c']

print(t2 is t) # Así sabemos si t y t2 apuntan al mismo objeto
print(t)
print(t2)
x = t.pop(1)
print(t2)

""" pop modifica la lista y regresa el elemento que fue removido. Si no provees un
índice, la función elimina y retorna el último elemento. """

x2 = t2.pop()
print(x2)
print(t2)
print(t)

""" Si no necesitas el valor removido, puedes usar el operador del: """
t = ['a', 'b', 'c']
del t[1]
print(t)

""" Si sabes qué elemento quieres eliminar (pero no sabes el índice), puedes usar
remove: """
t = ['a', 'b', 'c']
t.remove('c')
print(t)

# El valor de retorno de remove es None

""" Para remover más de un elemento, puedes usar del con un índice de rebanado: """
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)
""" Como siempre, el rebanado selecciona todos los elementos hasta, pero excluyendo,
el segundo índice. """