""" Contar cuántas veces aparece una letra en una cadena """
palabra = 'brontosaurio'
d = dict()
for c in palabra:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1

print(d)

""" El método 'get' de los diccionarios, toma una clave y un valor por defecto. Si la clave aparece, 'get' devuleve
    el valor correspondiente, si no, devuelve el valor por defecto. """
cuentas = {'Chuck' : 1, 'Annie' : 42, 'Jan' : 100}
print(cuentas.get('Jan', 0))
print(cuentas.get('Tim', 0))

""" Podemos usar 'get' para escribir nuestro programa de 'brontosaurio' (histograma) más conciso, puesto que el método
    'get' maneja el caso en que una clave no está en el diccionario, podemos reducir cuatro líneas a una y eliminar
    la sentencia 'if'. """
palabra = 'brontosaurio'
d = dict()
for c in palabra:
    d[c] = d.get(c, 0) + 1

print(d)