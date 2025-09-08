from flask import Flask, render_template, request, redirect
import pymysql
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configurar PyMySQL para que funcione como MySQLdb
pymysql.install_as_MySQLdb()

# Crear la conexión a la BD usando variables de entorno
class MySQL:
    def __init__(self):
        self.connection = None
    
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

@app.route('/')
def index():
    sql="SELECT * FROM equipos"

    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql)
    equipos=cursor.fetchall()
    conexion.commit()
    return render_template('sitio/index.html', equipos=equipos)


@app.route('/sitio/guardar', methods=['POST'])
def guardar():
    descripcion = request.form['descripcion']
    email= request.form['email']

    # Insertar datos en la BD
    sql="INSERT INTO equipos (descripcion, email) VALUES (%s, %s)"
    datos=(descripcion,email)
    conexion=mysql.connection

    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    return redirect ('/')


@app.route('/sitio/borrar/<int:id>')
def borrar(id):
    # Insertar datos en la BD
    sql="DELETE FROM equipos WHERE id=%s"
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql,(id,))
    conexion.commit()
    return redirect ('/')


@app.route('/sitio/editar/<int:id>')
def editar(id):    
    # Consulta para cargar los datos en el formulario
    sql="SELECT * FROM equipos WHERE id=%s"
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql,(id,))
    equipos=cursor.fetchone()
    conexion.commit()
    return render_template ('sitio/editar.html', equipos=equipos)

@app.route('/sitio/actualizar', methods=['POST'])
def actualizar():
    id= request.form['codigo']
    descripcion = request.form['descripcion']
    email= request.form['email']

    # Insertar datos en la BD
    sql="UPDATE equipos SET descripcion=%s, email=%s WHERE id=%s"
    datos=(descripcion,email,id)

    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    return redirect ('/')

if __name__ == '__main__':
    app.run(debug=True)