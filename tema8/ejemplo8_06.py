# Métodos de listas

# append(), agrega un nuevo elemento al final de una lista:

t = ['a', 'b', 'c']

print(t)

t.append('d')

print(t)

# extend(), toma una lista como argumento y agrega todos los elementos:

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']

print(t1)

t1.extend(t2)

print(t1)

# sort(), ordena los elementos de la lista de menor a mayor

t3 = ['d', 'c', 'e', 'b', 'a']

print(t3)

t3.sort()

print(t3)

""" La mayoría de métodos no regresan nada; modifican la lista y regresan None. Si
accidentalmentes escribes t = t.sort(), vas a decepcionarte con el resultado. """
t4 = ['z', 'q', 'a', 'l', 'j']

t4 = t4.sort()
print(t4)





















