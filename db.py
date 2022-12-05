# INSERT INTO user (nombre, edad, genero) VALUES ('Jose', '10', 'masculino')
# UPDATE users (nombre, edad, genero) VALUES ('Jose', '10', 'masculino') WHERE name = 'Jose'
# SELECT * FROM users WHERE edad = 10

#orm (objet relation and model ): herramienta los objetos que definimos como clases a su contraparte en una base de datos.
#orm alchemy

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property

base = declarative_base()

class Alumno(base):
    #cual es el nombre de la tabla que esta clase representa
    __tablename__ = 'alumnos'

    id = Column(Integer, primary_key=True)
    nombres = Column(String, nullable = False)
    apellidos = Column(String, nullable = False)
    carnet = Column(Integer)
    notas = relationship('Nota', back_populates='alumno')

    @hybrid_property
    def nombre_completo(self):
        return f'{self.nombres} {self.apellidos}'

class Nota(base):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key = True)
    curso = Column(String)
    nota = Column(Integer)
    alumno_id = Column(Integer, ForeignKey('alumnos.id'))
    alumno = relationship('Alumno', back_populates = 'notas')

engine = create_engine('sqlite:///:memory:')

base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

ana = Alumno(
    nombres = 'Ana',
    apellidos = 'Gomez',
    carnet = 1234,
)
print(ana.id)

#insert 
#guardad info en la base de datos 
session.add(ana)
#guarda la info permanentemente
session.commit()
#obtener info desde la base de datos
session.refresh(ana)
print(ana.id)

#Query o cosulta
ana_from_db = session.query(Alumno).where(Alumno.nombres == 'Ana').first()
print(ana_from_db.apellidos)

#Update o actualizacion
ana_from_db.carnet = 5678
session.add(ana_from_db)
session.commit()

#dalete borrado
#session.delete()
#session.commit()

luis = Alumno(
    nombres = ('Lius'),
    apellidos = ('Perez'),
    carnet = 4321,
)
session.add(luis)
session.commit()

# crear varios
alumnos = session.query(Alumno).all()
print(alumnos[0].nombres)
print(alumnos[1].nombres)

print(luis.nombre_completo)

nota = Nota(
    curso = 'matematicas',
    nota=89,
    alumno_id= luis.id,
)

session.add(nota)
session.commit()

session.refresh(nota)
print(nota.alumno.nombres)
session.refresh(luis)
print(luis.notas[0].nota)
print(nota.alumno.notas[0].alumno.nombre_completo)
