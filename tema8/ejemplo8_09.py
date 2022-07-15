""" Una cadena es una secuencia de caracteres y una lista es una secuencia de valores,
pero una lista de caracteres no es lo mismo que una cadena. Para convertir una
cadena en una lista de caracteres, puedes usar list: """

palabra = 'spam'

lista = list(palabra)

print(lista)

""" La función list divide una cadena en letras individuales. Si quieres dividir una
cadena en palabras, puedes utilizar el método split: """

palabras = 'Suspirando por los fiordos'

t = palabras.split()

print(t)

print(t[2]) # puedes utilizar el operador índice (corchetes) para ver una palabra en particular en la lista.

""" Puedes llamar split con un argumento opcional llamado delimitador que especifica
qué caracteres usar para delimitar las palabras. El siguiente ejemplo utiliza un
guión medio como delimitador: """

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)

print(t)

""" join es el inverso de split. Este toma una lista de cadenas y concatena los
elementos. join es un método de cadenas, así que tienes que invocarlo en el
delimitador y pasar la lista como un parámetro: """

s = ['Suspirando', 'por', 'los', 'fiordos']
print(s)
delimitador = ' '
t = delimitador.join(s)

print(t)








