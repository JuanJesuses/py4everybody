""" Ejercicio 1: Escribe un programa que lea repetidamente números hasta
que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
muestra por pantalla el total, la cantidad de números y la media de
esos números. Si el usuario introduce cualquier otra cosa que no sea un
número, detecta su fallo usando try y except, muestra un mensaje de
error y pasa al número siguiente. """

total = 0
cantidad = 0
interruptor = ''

while interruptor != 'fin':
    num = input('Introduce el número: ')
    try:
        numero = int(num) # Convertimos la variable al tipo que necesitemos
        cantidad = cantidad + 1
        total = total + numero   
    except:
        print('ERROR!!! Introduzca sólo valores numéricos')
    interruptor = input('¿Quieres introducir otro número? (fin para terminar): ')

print('La suma total de los números introducidos es: {}'.format(total))
print('La cantidad de números introducidos es: {}'.format(cantidad))
try:
    print('La media de los números introducidos es: {}'.format(round(total/cantidad, 2)))
except:
    print('ERROR!! No se puede dividir entre cero') 