from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    correo = Column(String)
    telefono = Column(String)
    tipo_usuario = Column(String)
    contrasena = Column(String)

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', apellido='{self.apellido}', correo='{self.correo}', telefono='{self.telefono}', tipo_usuario='{self.tipo_usuario}')>"