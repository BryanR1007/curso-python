class Member:
    #parametros
    altura = None
    imc = None
    name = None
    #metodos de la clase.
    #init es un constructor.
    #metodo constructor.
    #self se refiere a si mismo.
    def __init__(self, name):
        self.name = name

    def register(self):
        print('usuario regstrado')

    def welcome(self):
        print(f'hola, bienvenido {self.name}')
        
#jose = Member()        
jose = Member('Jose')
#jose.name='Jose'
pablo = Member('Pablo')
#pablo.name = 'Pablo'
jose.altura=172
jose.imc=15
print(jose.altura)
print(jose.imc)
print(jose.name)
jose.register()
print(type(jose))
jose.welcome()
pablo.welcome()

# Herencia
#Ejemplo basado en un gim
class Person():
    firs_name = None
    last_name = None
    birthdate = None

    def be_in_gim(self):
        print('Estoy en el gimnacio')

class Trainer(Person):
    salary = None

    def be_in_gim(self):
        print('Estoy trabajando')

class Member(Person):
    imc = None

    def be_in_gim(self):
        print('Estoy ejercitandome')

alumno = Member()
alumno.be_in_gim()


#ejemplo de clases: sistema de control de vehivulos
#A ABC = bstract base clas
#clase abstracta

from abc import ABC, abstractmethod

class Vehicule(ABC):
    puertas = None
    llantas = None

    @abstractmethod
    def avanzar(self):
        pass

class Car(Vehicule):
    puertas = 5
    llantas = 4
    
    def avanzar(self):
        return 'avanzo en 4 ruedas'


class moto(Vehicule):
    puertas = 0
    llantas = 2

    def avanzar(self):
        print(f'avanzo en {self.llantas} ruedass')    

    #es es un metodo-string    
    def __str__(self):
        return f'esta es una moto con {self.puertas} puertas y {self.llantas} ruedas'

#vehiculo = Vehicule()
#vehiculo.avanzar()
carro = Car()
print(carro.puertas)
motocicleta = moto()
motocicleta.avanzar()
print(motocicleta)

# __nombre es para ocultar 
class User():
    contrasena = 'contrasena-encriptada'

    def __init__(self) -> None:
        self.contrasena = self.__desencriptar()

    def __desencriptar(self):
        return 'contrasena-desencriptada'
    
usuario = User()
#print(usuario.__desencriptar())
print(usuario.contrasena)

#polimorfismo: capacidad de transformar su comportamiento dependiendo de sus caracteristicas.
#encapsulacion: es la capacidad de poder restringir ciertos atributos y metodos solamente al objeto



