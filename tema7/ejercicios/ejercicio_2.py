""" Ejercicio 2: Escribe un programa que solicite un nombre de archivo
y después lea ese archivo buscando las líneas que tengan la siguiente
forma:
X-DSPAM-Confidence: 0.8475
**Cuando encuentres una línea que comience con “X-DSPAM-Confidence:” ponla
aparte para extraer el número decimal de la línea. Cuenta esas líneas y después
calcula el total acumulado de los valores de “spam-confidence”. Cuando llegues al
final del archivo, imprime el valor medio de “spam confidence”. 
Prueba tu programa con los archivos mbox.txt y mbox-short.txt. """

# Solicitamos el nombre del archivo
nom_archivo = input('Introduzca un  nombre de archivo: ')

# Capturamos la excepción en caso de error
try:
    archivo = open(nom_archivo)
except:
    print('No se puede abrir el archivo: ', archivo)
    exit()
    
contador_lineas = 0
suma_dir = 0.0
lista_num = [] # Para comprobar que se almacenan los valores numéricos correctamente

for linea in archivo:
    direccion_num = linea # almacenamos cada linea en direccion_num para operar con ella
    if not linea.startswith('X-DSPAM-Confidence: '):
        continue
    contador_lineas = contador_lineas + 1
    posicion_dp = linea.find(':') # localizamos los dos puntos para encontrar el valor numérico
    posicion_num = linea.find(' ', posicion_dp) # localizamos el espacio en blanco despues de los dos puntos
    # direccion_num = linea[posicion_dp + 1 : ]
    direccion_num = float(linea[posicion_num + 1 : ])
    lista_num.append(direccion_num)
    suma_dir = suma_dir + direccion_num
    
print(type(lista_num[0])) # Comprobamos que se almacenan como tipo float
suma_dir = contador_lineas / suma_dir
print('Promedio spam confidence: ', suma_dir)

archivo.close()
    
    
    
    
    
    
    
    
    
    
    
    
    