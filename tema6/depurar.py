# Programa funcional pero que falla si se introduce una línea en blanco
""" while True:
    linea = input("> ")
    if linea[0] == '#':
        continue
    if linea == 'fin':
        break
    print(linea)
print('Terminado!') """ 

# Programa que corrije el error anterior con la sentencia linea.starswith
""" while True:
    linea = input('> ')
    if linea.startswith('#'):
        continue
    if linea == 'fin':
        break
    print(linea)
print('Terminado!!') """

# Otra versión que corrije el error anterior con la función len
while True:
    linea = input("> ")
    if len(linea) > 0 and linea[0] == '#':
        continue
    if linea == 'fin':
        break
    print(linea)
print('Terminado!')