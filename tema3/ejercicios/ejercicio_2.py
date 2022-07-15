""" Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
    programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
    un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
    del programa: """

try:
    horas = float(input("Introduzca el número de horas: "))
    tarifa_hora = float(input("Introduce la tarifa por horas: "))
    horas_intermedias = horas - 40 # El número de horas trabajadas que exceden de 40
    tarifa_hora_intermedia = tarifa_hora * 1.5 # El valor de la hora intermedia que es un 1.5 más que la hora normal
    salario_intermedio = horas_intermedias * tarifa_hora_intermedia # El precio al que hay que pagar las horas que exceden de 40 horas
    salario = 0

    if horas > 40:
        salario = (tarifa_hora * 40) + salario_intermedio
    else:
        salario = tarifa_hora * horas
    print('El salario es: ', salario)
except:
    print('Error, por favor introduzca un número.')

