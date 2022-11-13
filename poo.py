class Member:
    altura = None
    imc = None
    name=None

    def __init__(self, name):
        self.name = name

    def register(self):
        print('usuario regstrado')

    def welcome(self):
        print(f'hola, bienvenido {self.name}')

persona = Member('Jose')

#persona = Member()
persona.altura=172
persona.imc=15
#persona.name='Jose'
print(persona.altura)
print(persona.imc)
print(persona.name)
persona.register()
print(type(persona))
persona.welcome()
