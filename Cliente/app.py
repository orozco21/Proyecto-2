from flask import Flask, render_template, request
import datetime

import requests


app = Flask(__name__)
# Datos de ejemplo de usuarios
users = {'empleado@atlas.com': 'password123', 'admin': '12345'}


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
  
    if username in users and users[username] == password:
        # return 'Inicio de sesión exitoso'
        # codigo = '12345'  # Código de ejemplo
        codigo = username
        fecha= datetime.datetime.now()
        servidor='/enviar'
        if username=='empleado@atlas.com':
            name='John Doe'
        else:
            name=codigo
        # return render_template('codigo.html', codigo=codigo)
        return render_template('codigo.html', codigo=codigo,fecha=fecha,servidor=servidor,name=name)
    else:
        return '<script>alert("Credenciales incorrectas");</script>'+ render_template('login.html')


@app.route('/enviar', methods=['POST'])
def enviar_datos():
    nombre = request.form['nombre']
    correo = request.form['correo']
    fecha = request.form['fecha']
    url = 'http://127.0.0.1:5001/personas'  # Reemplaza con la URL de tu servicio RESTful
    datos = {'nombre': nombre, 'correo': correo, 'fecha':  fecha}  # Los datos que quieres enviar
    
    response = requests.post(url, json=datos)
    
    if response.status_code == 200:
        print('Datos enviados correctamente')
    else:
        print('Error al enviar los datos')


if __name__ == '__main__':
    app.run(debug=True)       
