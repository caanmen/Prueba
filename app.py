from flask import Flask, request, jsonify
from DatabaseConnection import DatabaseConnection
from UserService import UserService
from ReservaManager import ReservaManager

app = Flask(__name__)

# Configura aquí los detalles de tu base de datos
DB_HOST = "localhost"
DB_NAME = "Restaurante"
DB_USER = "postgres"
DB_PASSWORD = "adm"
DB_PORT = 5432 

db_connection = DatabaseConnection(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
user_service = UserService(db_connection)

@app.route('/')
def home():
    return 'Bienvenido a la API de ReservaFacil!'

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario_endpoint():
    data = request.json
    try:
        user_service.crear_usuario(data)
        return jsonify({"mensaje": "Usuario creado exitosamente."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
