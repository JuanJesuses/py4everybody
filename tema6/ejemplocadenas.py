palabra = input('Introduce una cadena: ')

palabra = palabra.lower()

print(palabra)

if palabra < 'banana':
    print('Tu palabra '+palabra+', está antes de banana')
elif palabra > 'banana':
    print('Tu palabra '+palabra+', está después de banana')
else:
    print('Tu palabra es banana')