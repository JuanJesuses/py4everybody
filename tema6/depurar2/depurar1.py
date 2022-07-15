# Programa original donde se vio el funcionamiento del bucle While 

"""while True:
    linea = input('> ')
    if linea[0] == '#': # Si se deja una línea vacía el código falla
      continue
    if linea == 'fin':
        break
    print(linea)
print('¡Terminado')"""

# Programa que soluciona lo de la lñinea vacía
while True:
    linea = input('> ')
    if linea.startswith('#'): # Esto obliga a introducir la almohadilla o continuar el programa
      continue
    if linea == 'fin':
        break
    print(linea)
print('¡Terminado') 