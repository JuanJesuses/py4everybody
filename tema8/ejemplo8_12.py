""" DUDA DEL EJEMPLO 8_7 RESUELTA!!!!!!!
    Si a se refiere a un objecto y tu asignasb = a, entonces ambas variables se refieren
    al mismo objeto:"""
a = [1, 2, 3]
b = a
print (b is a)

""" La asociación de una variable a un objeto es llamada una referencia. En este
ejemplo, hay dos referencias al mismo objeto.
Un objeto con más de una referencia tiene más de un nombre, así que decimos que
el objeto es un alias.
Si el alias del objeto es mutable, los cambios hechos a un alias afectan al otro: """
b[0] = 17
print(a)

""" Aunque este comportamiento puede ser útil, es propenso a errores. En general, es
más seguro evitar usar alias cuando estás trabajando con objetos mutables.
Para objetos inmutables como cadenas, los alias no son un problema realmente. """

""" En este ejemplo casi nunca hay diferencia si a y b apuntan a la misma cadena o no: """

a = 'banana'
b = 'banana'