""" Bucle para imprimir una clave con su valor correspondiente """
contadores = {'chuck' : 1, 'Annie' : 42 , 'Jan' : 100}
for clave in contadores:
    print(clave, contadores[clave])

# Podemos utilizar este patrón para realizar otro tipo de búsquedas, por ejemplo, claves cuyo valor sea mayor que 10
contadores = {'chuck' : 1, 'Annie' : 42 , 'Jan' : 100}
for clave in contadores:
    if contadores[clave] > 10:
        print(clave, contadores[clave])

""" Para imprimir las claves (en este caso) en orden alfabético, hacemos una lista de las claves del diccionario
    con el método 'keys' disponible en los objetos del diccionario, después ordenar esa lista e iterar a través de 
    la lista ordenada buscando cada clave e impriendo los pares clave - valor """
contadores = {'Chuck' : 1, 'Annie' : 42 , 'Jan' : 100}
lst = list(contadores.keys()) # El método keys devuelve las claves del diccionario que guardamos como lista en lst
print(lst)
lst.sort()
for clave in lst:
    print(clave, contadores[clave])