import sys
import os
import logicos
#sys.path.append('./modulo_interior')
from modulo_interior import interior, object_interior
from modulo_interior.interior import saludo
from logicos import verificar_edad, EDAD_MINIMA
from logicos import *
import modulo_main

#import generaciones as g
#generaciones = 1

#print(logicos.edad)
#logicos.verificar_edad()

#print(EDAD_MINIMA)
#print(EDAD_MAXIMA)

#print(modulo_interior.interior.saludo)
#print(sys.path)
print(interior.saludo)
print(object_interior)

#print(os.getenv('PYTHONPATH'))

#os.environ['PYTHONPATH'] = 'valor diferente'
print(os.getenv('PYTHONPATH'))
#print(dir())
print(modulo_main.saludarnombre('Pedro'))



            # caso si necesito validar si un modulo existe
try:
    import moduloquenoexiste
except ModuleNotFoundError as e:
    print('Disculpe este modulo no esta disponible' , e)