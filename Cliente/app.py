from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Aquí puedes añadir la lógica para autenticar al usuario
    # y generar el código de respuesta

    codigo = '12345'  # Código de ejemplo

    return render_template('codigo.html', codigo=codigo)

if __name__ == '__main__':
    app.run(debug=True)