numero = 1

while numero <= 10:
    print(numero)
    numero += 1

perros = ['Bobby', 'Rex', 'Max', 'Avellana']
numero = 1
for perro in perros: 
    print(perro)

while numero <= 10:
    if numero == 5:
        break
    print(numero)
    numero += 1

perros = ['Bobby', 'Rex', 'Max', 'Avellana']
numero = 1
for perro in perros: 
    if perro == 'Max':
        print('Este es el perro')
        continue

    print('Este no es el perro')