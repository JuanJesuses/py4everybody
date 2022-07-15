""" Cuando pasas una lista a una función, la función obtiene un apuntador a la lista.
Si la función modifica un parámetro de la lista, el código que ha llamado la función
también verá el cambio. Por ejemplo, remover_primero elimina el primer elemento
de una lista: """

def remover_primero(t):
    del t[0]

""" Aquí está el ejemplo de cómo se usa: """

letras = ['a', 'b', 'c']
#print(letras)
remover_primero(letras)
print(letras)

# El parámetro t y la variable letras son alias para el mismo objeto.

""" Es importante distinguir entre operaciones que modifican listas y operaciones que
crean nuevas listas. Por ejemplo, el método append modifica una lista, pero el
operador + crea una nueva lista: """
t1 = [1, 2]
t2 = t1.append(3) # imprime None porque la mayoría de los métodos no devuelven nada;

print(t1)
print(t2) # modifican la lista y devuelven None, pero se trata del mismo objeto.

t1 = [1, 2] # volvemos a asignar para no duplicar el 3
t3 = t1 + [3]
print(t3)
print(t2 is t3)

""" Esta diferencia es importante cuando escribes funciones que no están destinadas a
modificar listas. Por ejemplo, esta función no elimina el primer elemento de una
lista: 

El operador de rebanado crea una nueva lista y el asignamiento hace que t apunte
a la lista, pero nada de esto tiene efecto en la lista que fue pasada como argumento."""
def mal_eliminar_primero(t):
    t = t[1:]
    print(t)

letras = ['a', 'b', 'c']

mal_eliminar_primero(letras)
print(letras) # Se imprime como tal porque el reabanado crea una lista nueva, no modifica la que se pasa por parámetro a la función.

""" Una alternativa es escribir una función que cree y regrese una nueva lista. Por
ejemplo, cola regresa todo excepto el primer elemento de una lista: """

def cola(t):
    return t[1:]

# Esta función deja la lista original sin modificar. Aquí está como se usa:

letras = ['a', 'b', 'c']
resto = cola(letras)
print(resto)
print(letras)











