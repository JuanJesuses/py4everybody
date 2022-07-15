""" Ejercicio 1: Escribe una función llamada recortar que toma una lista y la modi-
fica, removiendo el primer y último elemento, y regresa None. Después escribe una
función llamada medio que toma una lista y regresa una nueva lista que contiene
todo excepto el primero y último elementos. """

def recortar(t):
    t.pop(0)
    t.pop()
    

def medio(t):
    longitud = len(t)
    return t[1:longitud - 1]

lista = ['a', 'b', 'c', 'd', 'e', 'f']

print(recortar(lista))

print(medio(lista))   