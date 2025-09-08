from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
CORS(app)  # Habilitar CORS para el frontend

# Configurar PyMySQL para que funcione como MySQLdb
pymysql.install_as_MySQLdb()

# Crear la conexión a la BD usando variables de entorno
class MySQL:
    def __init__(self):
        pass
    
    def init_app(self, app):
        pass
    
    @property
    def connection(self):
        return pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'proyectowebflask'),
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

mysql = MySQL()
mysql.init_app(app) 

@app.route('/api/equipos', methods=['GET'])
def index():
    sql="SELECT * FROM equipos"
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql)
    equipos=cursor.fetchall()
    conexion.commit()
    return jsonify(equipos)

@app.route('/api/equipos', methods=['POST'])
def guardar():
    data = request.get_json()
    descripcion = data['descripcion']
    email = data['email']

    # Insertar datos en la BD
    sql="INSERT INTO equipos (descripcion, email) VALUES (%s, %s)"
    datos=(descripcion,email)
    conexion=mysql.connection

    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    return jsonify({'success': True, 'message': 'Equipo creado correctamente'})

@app.route('/api/equipos/<int:id>', methods=['DELETE'])
def borrar(id):
    # Eliminar equipo de la BD
    sql="DELETE FROM equipos WHERE id=%s"
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql,(id,))
    conexion.commit()
    return jsonify({'success': True, 'message': 'Equipo eliminado correctamente'})

@app.route('/api/equipos/<int:id>', methods=['GET'])
def editar(id):    
    # Consulta para obtener los datos del equipo
    sql="SELECT * FROM equipos WHERE id=%s"
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql,(id,))
    equipos=cursor.fetchone()
    conexion.commit()
    return jsonify(equipos)

@app.route('/api/equipos/<int:id>', methods=['PUT'])
def actualizar(id):
    data = request.get_json()
    descripcion = data['descripcion']
    email = data['email']

    # Actualizar datos en la BD
    sql="UPDATE equipos SET descripcion=%s, email=%s WHERE id=%s"
    datos=(descripcion,email,id)

    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    return jsonify({'success': True, 'message': 'Equipo actualizado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)