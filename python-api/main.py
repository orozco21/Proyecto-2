from  flask import Flask, jsonify, request
import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    port = 3306,
    database = 'personas'
)

cursor = connection.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    return 'Holaaaaaaaaaaaaaaaaaaa'

@app.route('/personas', methods = ["GET"])
def get_personas():
    sql = "SELECT * FROM personas"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return jsonify(result)

@app.route('/personas/<id_persona>', methods = ["GET"])
def get_persona(id_persona):
    sql = "SELECT * FROM personas WHERE _id = " + str(id_persona)
    cursor.execute(sql)
    result = cursor.fetchone()
    
    return jsonify(result)

@app.route('/personas', methods = ["POST"])
def create_persona():
    nombre = request.form['nombre']
    correo = request.form['correo']
    fecha = request.form['fecha']
    try:
        sql = f"INSERT INTO personas (id,nombre, correo,fecha) VALUES (NULL,'{nombre}', '{correo}','{fecha}')"
        cursor.execute(sql)
        connection.commit()
        
        return jsonify({
            "status": 1,
            "respond": "Persona creada correctamente"
        })
    except Exception as e:
        return jsonify({
            "status": 0,
            "respond": "Ha ocurrido un error al insertar el registro"
        })
        
@app.route('/personas/<id_persona>', methods = ["PUT"])
def edit_persona(id_persona):
    nombre = request.form['nombre']
    celular = request.form['celular']
    
    try:
        sql = f"UPDATE personas SET nombre = '{nombre}', celular = {celular} WHERE _id = {id_persona}"
        cursor.execute(sql)
        connection.commit()
        
        return jsonify({
            "status": 1,
            "respond": "Persona editada correctamente"
        })
    except Exception as e:
        return jsonify({
            "status": 0,
            "respond": "Ha ocurrido un error al editar el registro"
        })

@app.route('/personas/<id_persona>', methods = ["DELETE"])
def delete_persona(id_persona):
    try:
        sql = f"DELETE FROM personas WHERE _id = {id_persona}"
        cursor.execute(sql)
        connection.commit()
        
        return jsonify({
            "status": 1,
            "respond": "Persona eliminada correctamente"
        })
    except Exception as e:
        return jsonify({
            "status": 0,
            "respond": "Ha ocurrido un error al eliminar el registro"
        })
    
        
    

if __name__ == '__main__':
    app.run(debug = True, port=5001)