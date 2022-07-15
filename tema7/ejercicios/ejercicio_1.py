""" Ejercicio 1: Escribe un programa que lea un archivo e imprima su con-
tenido (línea por línea), todo en mayúsculas. Al ejecutar el programa,
debería parecerse a esto: """

# Capturamos la excepción en caso de que no exista o no esté escrito correctamente
try:
    capL_arch = open('/home/john/eclipse-workspace/ejercicios_libro/tema7/mbox-short.txt')
except:
    print('No se puede abrir el archivo', capL_arch)
    exit()

# Recorremos el archivo para leerlo línea a línea
for linea in capL_arch:
    longitud = len(linea) # Esta línea sólo es necesaria para la opción 2
    
    # Opción 1:
    if linea.find('\n') == -1:
        continue
    linea = linea.rstrip()
    print(linea.upper())
    """
    #Opción 2:
    if len(linea) < longitud-1:
        continue
    linea = linea.rstrip()
    print(linea.upper())"""

capL_arch.close()    