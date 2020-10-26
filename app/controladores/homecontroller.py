"""
Este archivo maneja las solicitudes del cliente para los datos del usuario del sistema
"""

from flask import request, render_template, flash
from app.models.usuarios_model import usuario


class HomeController:
    """ """
    def __init__(self):
        pass

    def index(self):
        """ Esta función ayuda a renderizar la página principal del sistema"""
        user = {'nickname': 'kb'}
        return render_template('index.html', title='Inicio', user=user)

    def registro(self):
        """ Esta función ayuda a renderizar el registro de usuarios """
        return render_template("cuentas/registro.html", title='Registro')

    def registro_usuario(self):
        """ Esta función envía los datos del usuario a la capa de modelo para insertar en la base de datos"""

        _nombre = request.form['nombre']
        _apellidos = request.form['apellidos']
        _email = request.form['email']
        _password = request.form['password']

        usuario.registrar_usuario(_nombre, _apellidos, _email, _password)
        return render_template('cuentas/registro.html', title="Registro")

    def login(self):
        return render_template("cuentas/login.html", title="Inicio de Sesión")

    def ver_inicio_sesion(self):
        return render_template("paginas/inicio_usuario.html", title="Inicio")

    def iniciar_sesion(self):
        _email = request.form['email']
        _password = request.form['password']

        user = usuario.ini_sesion(_email, _password)

        if usuario:
            flash(user[0][1])
            return render_template('paginas/inicio_usuario.html')
        else:
            flash('El usuario o la contraseña son incorrectos')
            return render_template('cuentas/login.html')

homecontroller = HomeController()

