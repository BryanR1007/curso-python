def sumar():
    return 3 + 2

print("la respuesta es: 5")
numero = sumar()

if numero == 5:
    print('Si es 5')
else:
    print('no es un 5')

x = 0
while x < 3:
    print(x)
    x += 1

for i in range(3):
    print(i)

for i in range(3):
    if i == 1:
        continue
    print(i)

#print(True)
#print(False)

edad = 15
def isadult(age):
    return age >= 18
print(isadult(15))
print(isadult(20))

print(None)

def vacio():
    pass
print(vacio())

print(True and False)
print(True or False)
print(not True)

if not isadult(15):
    print('no es un adulto')