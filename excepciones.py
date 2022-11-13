# son errores que no deberian pasar


edad = 17

if edad < 18:
    raise Exception('Eres menor')

print('continuacion')

class AgeException(Exception):
    pass


try:
    'texto' + 5
    if edad <18:
        raise AgeException('Eres menor')

except Exception:
    print('Se lanzo el error')