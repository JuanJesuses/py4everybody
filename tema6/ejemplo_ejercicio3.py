""" Ejercicio 3: Encapsula este código en una función llamada cuenta, y
hazla genérica de tal modo que pueda aceptar una cadena y una letra
como argumentos. """

def cuenta_letras(cadena, letra):

	contador = 0

	for i in cadena:
		if i == letra:
			contador = contador + 1

	return contador

palabra = input('Introduce una palabra: ')
letras = input('¿Qué letra quieres contar?: ')

total = cuenta_letras(palabra, letras)

print('Hay {} letras {}'.format(total, letras))