""" Ejercicio 5: Escribe un programa que le pida al usuario una temperatura en grados Celsius,
    la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida. """

grados_f = 33.8

grados_c = float(input("Introduce los grados celsius para pasar a Farenheit: "))

grados_convertidos = round((grados_c * grados_f), 2)

print(grados_convertidos, 'grados Farenheit')