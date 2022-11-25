class Member:
    altura = None
    imc = None
    name = None

    def __init__(self, name):
        self.name = name

    def register(self):
        print('usuario regstrado')

    def welcome(self):
        print(f'hola, bienvenido {self.name}')


        
#persona = Member()        
persona = Member('Jose')
persona2 = Member('Pablo')
#persona2.name = 'Pablo'
#persona.name='Jose'

persona.altura=172
persona.imc=15
print(persona.altura)
print(persona.imc)
print(persona.name)
persona.register()
print(type(persona))
persona.welcome()
persona2.welcome()
