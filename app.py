from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
#Crear la conexion a la BD
mysql = MySQL()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectowebflask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
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

    #Insertar datos en la BD
    sql="INSERT INTO equipos (descripcion, email) VALUE (%s, %s)"
    datos=(descripcion,email)
    conexion=mysql.connection

    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    return redirect ('/')


@app.route('/sitio/borrar/<int:id>')
def borrar(id):
    #Insertar datos en la BD
    sql="DELETE FROM equipos WHERE id=%s"
    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql,(id,))
    conexion.commit()
    return redirect ('/')


@app.route('/sitio/editar/<int:id>')
def editar(id):    
    #Consulta para cragar los datos en el formulario
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

    #Insertar datos en la BD
    sql="UPDATE equipos SET descripcion=%s, email=%s WHERE id=%s"
    datos=(descripcion,email,id)

    conexion=mysql.connection
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    return redirect ('/')

if __name__ == '__main__':
    app.run(debug=True)