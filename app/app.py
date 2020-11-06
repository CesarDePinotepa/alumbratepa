import os
import hashlib

from functools import wraps

from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')


# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'alumbradopino'

mysql = MySQL(app)

# settings
# app.secret_key = b'llave7secreta'


from app.models.usuarios_model import traer_usuario
import app.models.reporte_model as r


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    """

    """
    try:
        error = ''
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user_data = traer_usuario(email=email, _password=password)

            # cifrar el password
            h = password.encode('utf-8')
            encode_pass = hashlib.md5(h)

            if email == user_data[0][3] and encode_pass.hexdigest() == user_data[0][5]:
                session['logged_in'] = True
                session['username'] = user_data[0][1]
                return render_template('paginas/inicio_usuario.html', title="Inicio", error=error, user=user_data[0][1],
                                       user_id=user_data[0][0])
            else:
                print('La contraseña o el usuario son incorrectos')
                error = 'La contraseña o el usuario son incorrectos.'
        return render_template('cuentas/login.html', error=error, title="Inicio de Sesión")

    except Exception as err:
        return render_template('cuentas/login.html', error=str(err))


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        """login session"""
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            pass
        return redirect(url_for('login'))
    return wrap


app.secret_key = b'llave7secreta'


@login_required
@app.route('/reportes')
def reportes():
    """
    Redireccionar a la vista de todos los reportes
    """
    reportes_data = r.traer_todos_los_reportes()
    return render_template('paginas/reporte.html', reportes=reportes_data)


@app.route('/inicio')
@login_required
def user_dash():
    return render_template('paginas/inicio_usuario.html')


@app.route('/mis-resportes/<user_id>')
@login_required
def mis_reportes(user_id):
    """

    """
    reportes_data = r.traer_reportes_por_usuario(user_id)
    return render_template('paginas/reportes_user.html', reportes=reportes_data)


@app.route('/nuevo-reporte')
@login_required
def nuevo_reporte():
    """
    """
    data = [{'name': 'Apagado'}, {'name': 'Foco Roto'}, {'name': 'Poste Caido'}, {'name': 'Cable Caido'}]
    return render_template('paginas/add_reporte.html', datos=data)


@app.route('/agg-reporte', methods=['POST'])
@login_required
def agregar_reporte():
    """"
    """
    try:
        if request.method == 'POST':
            select = request.form['mal']
            direccion = request.form['direccion']
            comentario = request.form['comentario']
            user_id = request.form['user_id']

            datos_insertados = r.insertar_reporte(select, direccion, comentario, user_id)
            if datos_insertados:
                mensaje = ["verde", "Los datos se guardaron correctamente"]
            else:
                mensaje = ["rojo", "Los datos NO se pudieron guardar"]

            return redirect(url_for('nuevo_reporte', mensaje=mensaje))

    except Exception as err:
        return render_template('paginas/add_reporte.html', error=str(err))
