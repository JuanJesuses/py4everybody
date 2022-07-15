# Depuración

""" 1. No olvides que la mayoría de métodos de listas modifican el argumento y
regresan None. Esto es lo opuesto a los métodos de cadenas, que regresan
una nueva cadena y dejan la original sin modificar. """

lista_1 = ['a', 'b', 'c', 'd', 'e', 'f']
lista_2 = [1, 2, 3, 4, 5, 6, 7, 8]
lista_3 = [['a', 'b', 45, 'sentadilla'], 34, 56, 'j']

""" 2. Elige un estilo y apégate a él.
Parte del problema con listas es que hay demasiadas formas de hacer las
cosas. Por ejemplo, para remover un elemento de una lista, puedes utilizar
pop, remove, del, o incluso una asignación por rebanado.
Para agregar un elemento, puedes utilizar el método append o el operador +.
Pero no olvides que esos también son correctos: """


"""
def mala_suma(t, x):
    t = t + x
    return t


#t = lista_1.append(28)
#t = lista_1.append([28])

#t = lista_1.append(lista_3)
#t = lista_1.append([lista_3])

lista_1.append(54)
print(type(lista_1))
lista_1 = lista_1 + lista_3
print(type(lista_1))

lista_1 = lista_1.append(54)

t = lista_1
print(t)
t = t + lista_2 # Esto genera error porque t es un objeto None y lista_2 es una lista
print(t)"""

""" 3. Hacer copias para evitar alias.
Si quieres utilizar un método como sort que modifica el argumento, pero
necesitas mantener la lista original también, puedes hacer una copia. """














