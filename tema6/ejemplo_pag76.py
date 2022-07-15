""" Si queremos obtener la segunda parte de la dirección de un correo electrónico
     1. Encontramos la posición de la arroba en la cadena
     2. Encontramos la posición del primer espacio DEESPUÉS de la arroba
     3. Partimos la cadena para extraer la porción de la cadena que estamos buscando """

dato = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

arrobapos = dato.find('@') # Encontramos la posición de la arroba
print(arrobapos)

espos = dato.find(' ', arrobapos) # Encontramos la posición del primer espacio después de la arroba
print(espos)

direccion = dato[arrobapos+1:espos] # Extraemos la parte de la cadena que nos interesa
print(direccion)