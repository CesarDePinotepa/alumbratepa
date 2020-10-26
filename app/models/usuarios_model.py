#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Este archivo ayuda a manejar la estructura lógica de los datos del usuario con la base de datos
"""
import hashlib

from flask import flash, request, render_template, redirect, url_for
from ..app import mysql


class UsuarioModel():
    """Esta clase ayuda a """

    def __init__(self):
        pass

    def registrar_usuario(self, _nombre, _apellidos,  _email, _password):
        """Esta funcion guarda en la base de datos los datos relacionados al usuario"""
        if request.method == 'POST':
            password = _password.encode('utf-8')
            h = hashlib.md5(password)

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO `usuarios`( `nombre`, `apellidos`, `email`, `tipo`, `password`) VALUES (%s,%s,%s,%s,%s)",
                        (_nombre, _apellidos, _email, 0, h.hexdigest()))
            mysql.connection.commit()

            cur.close()
            flash('Contacto agregado correctamente')

    def ini_sesion(self, _email, _password):
        """"""
        if request.method == 'POST':
            password = _password.encode('utf-8')
            h = hashlib.md5(password)
            # obtener el usuario solicitado
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM `usuarios` WHERE `email` = %s AND `password` = %s AND `tipo` = %s",
                        (_email, h.hexdigest(), 0))
            # cur.execute("SELECT * FROM `usuarios`")
            data = cur.fetchall()
            cur.close()

            return data
            # print(len(data))
            # if data:
            #     flash(data[0][1])
            # else:
            #     flash("Usuario o contraseña incorrecta")


usuario = UsuarioModel()

