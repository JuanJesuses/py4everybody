""" sabemos que ambos a y b se refieren a una cadena, pero no sabemos si se refieren
o apuntan a la misma cadena. Hay dos estados posibles: """

a = 'banana'
b = 'banana'

""" Por un lado, a y b se refieren a dos objetos diferentes que tienen el mismo valor.
Por otro lado, apuntan al mismo objeto.
Para revisar si dos variables apuntan al mismo objeto, puedes utilizar el operador
is. """

print(a is b) # Esto dará True

""" En este ejemplo, Python solamente creó un objeto de cadena, y ambos a y b
apuntan a él.
Pero cuando creas dos listas, obtienes dos objetos diferentes: """

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # Esto dará False

""" En este caso podríamos decir que las dos listas son equivalentes, porque tienen
los mismos elementos, pero no idénticas, porque no son el mismo objeto. Si dos
objetos son idénticos, son también equivalentes, pero si son equivalentes, no son
necesariamente idénticos. """

