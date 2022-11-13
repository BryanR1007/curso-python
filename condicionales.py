from logging.handlers import RotatingFileHandler


edad = input('Ingrese su edad \n')

if int(edad) > 18:
    print ('tu eres mayor de edad')
elif int(edad) == 18:
    print('Tienes 18 exactos')
else:
    print('Tu eres menor de edad')

nombre = 'paco'
if nombre == 'paco':
# if nombre != 'paco':
    print('Si eres paco')

nombre = 'RaFaEl'
if nombre.upper() != 'RAFAEL':
    print('Que bueno que no eres rafael, bienvenido')
else:
    print('Siempre bienvenido')

nombre = 'RaFaEl '
if nombre.upper().strip() != 'RAFAEL':
    print('Que bueno que no eres rafael, bienvenido')
else:
    print('Que no puedes entrar!!')

    
