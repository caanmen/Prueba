from DatabaseConnection import DatabaseConnection
from UserModel import Usuario

class UserService:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def crear_usuario(self, data):
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        correo = data.get('correo')
        telefono = data.get('telefono')
        tipo_usuario = data.get('tipo_usuario')
        contrasena = data.get('contrasena')

        session = self.db_connection.get_session()
        try:
            nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, correo=correo, telefono=telefono, tipo_usuario=tipo_usuario, contrasena=contrasena)
            session.add(nuevo_usuario)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()