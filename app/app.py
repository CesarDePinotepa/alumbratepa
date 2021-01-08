import hashlib

from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')


# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'alumbradopino'

mysql = MySQL(app)

# settings
app.secret_key = b'llave7secreta'

from app.models.usuarios_model import traer_usuario, insertar_usuario, todos_los_usuarios, agregar_usuario, eliminar_user
import app.models.reporte_model as r



@app.route('/')
def main():
    reportes_data = r.traer_todos_los_reportes()
    return render_template('index.html', reportes=reportes_data)


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
                session['user_id'] = int(user_data[0][0])
                # verificamos el tipo de usuario
                if int(user_data[0][4]) == 0:
                    return render_template('paginas/inicio_usuario.html', title="Inicio", error=error, user_id=user_data[0][1])
                else:
                    return render_template('paginas/inicio_admin.html', title="Admin", error=error, user_id=user_data[0][1])
            else:
                if "username" in session:
                    return redirect(url_for(user_dash))
                print('La contraseña o el usuario son incorrectos')
                error = 'La contraseña o el usuario son incorrectos.'
        return render_template('cuentas/login.html', error=error, title="Inicio de Sesión")

    except Exception as err:
        return render_template('cuentas/login.html', error=str(err))


@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('login'))


@app.route('/reportes')
def reportes():
    """
    Redireccionar a la vista de todos los reportes
    """
    if "username" in session:
        user = session["username"]
        reportes_data = r.traer_todos_los_reportes()
        return render_template('paginas/reporte.html', reportes=reportes_data, user_id=user)
    else:
        return redirect(url_for("login"))


@app.route('/inicio')
def user_dash():
    if "username" in session:
        user = session["username"]
        reportes_data = r.traer_todos_los_reportes()
        return render_template('paginas/inicio_usuario.html', user_id=user, reportes=reportes_data)
    else:
        return redirect(url_for("login"))


@app.route('/inicio-admin')
def admin_dash():
    if "username" in session:
        user = session["username"]
        reportes_data = r.traer_todos_los_reportes()
        print("Cesar")
        return render_template('paginas/inicio_admin.html', user_id=user, reportes=reportes_data)
    else:
        return redirect(url_for("login"))


@app.route('/mis-resportes')
def mis_reportes():
    """

    """
    if "username" in session:
        user_id = session["username"]
        id_user = session['user_id']
        reportes_data = r.traer_reportes_por_usuario(id_user)
        return render_template('paginas/reportes_user.html', reportes=reportes_data, user_id=user_id)
    else:
        return redirect(url_for("login"))


@app.route('/nuevo-reporte', methods=['GET', 'POST'])
def nuevo_reporte():
    """"
    """
    if "username" in session:
        user = session['username']
        uid = session['user_id']
        try:
            if request.method == 'POST':
                select = request.form['mal']
                direccion = request.form['direccion']
                comentario = request.form['comentario']
                poste = request.form['poste']

                mensaje = r.insertar_reporte(select, direccion, comentario, uid, poste)

                flash(mensaje)
                return redirect(url_for('nuevo_reporte'))
            else:
                data = [{'name': 'Apagado'}, {'name': 'Foco Roto'}, {'name': 'Poste Caido'}, {'name': 'Cable Caido'}]
                return render_template("paginas/add_reporte.html", datos=data, user_id=user)

        except Exception as err:
            return render_template('paginas/add_reporte.html', error=str(err))

    else:
        return redirect(url_for("login"))


@app.route('/registrar', methods=["GET", "POST"])
def registrar():
    """

    :return:
    """
    try:
        if request.method == "POST":
            nombre = request.form['nombre']
            apellidos = request.form['apellidos']
            email = request.form['email']
            password = request.form['password']

            mensaje = insertar_usuario(nombre, apellidos, email, password)
            flash(mensaje)
            return redirect(url_for('registrar'))
        else:
            return render_template("cuentas/registro.html", messages='')

    except Exception as err:
        return render_template("cuentas/registro.html", messages=err)


@app.route('/mis-usuarios')
def mis_usuarios():
    """

    """
    if "username" in session:
        user_id = session["username"]
        usuarios = todos_los_usuarios()
        return render_template('paginas/mis_usuarios.html', usuarios=usuarios, user_id=user_id)
    else:
        return redirect(url_for("login"))


@app.route('/nuevo-usuario', methods=["GET", "POST"])
def nuevo_usuario():
    """"
    """
    if "username" in session:
        user = session['username']
        try:
            if request.method == 'POST':
                select = request.form['user']
                nombre = request.form['nombre']
                apellido = request.form['apellido']
                password = request.form['password']
                email = request.form['email']

                mensaje = agregar_usuario(nombre, apellido, email, password, select)

                flash(mensaje)
                return redirect(url_for('nuevo_usuario'))
            else:
                data = [{'name': 'Normal'}, {'name': 'Admin'}]
                return render_template("paginas/add_usuario.html", datos=data, user_id=user)

        except Exception as err:
            return render_template('paginas/add_usuario.html', error=str(err))

    else:
        return redirect(url_for("login"))


@app.route('/eliminar-usuario/<uid>', methods=["GET", "POST"])
def eliminar_usuario(uid):
    """

    :param id:
    :return:
    """
    mensaje = eliminar_user(int(uid))
    # mensaje = str(type(int(uid)))
    flash(mensaje)
    return redirect(url_for('mis_usuarios'))


@app.route('/admin-resportes')
def admin_reportes():
    """

    """
    if "username" in session:
        user_id = session["username"]
        id_user = session['user_id']
        reportes_data = r.traer_todos_los_reportes()
        return render_template('paginas/admin_reporte.html', reportes=reportes_data, user_id=user_id)
    else:
        return redirect(url_for("login"))
