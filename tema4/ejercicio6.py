def calculo_salario(horas, tarifa):
    salario = horas * tarifa
    return salario

hora_emple = float(input('Introduzca las horas trabajadas: '))
tarifa_emple = float(input('Introduzca el precio por hora del empleado: '))

total = calculo_salario(hora_emple, tarifa_emple)

print((total))