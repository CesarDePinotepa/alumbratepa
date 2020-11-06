#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Este archivo ayuda a manejar la estructura lógica de los datos del usuario con la base de datos
"""

import hashlib

from app.app import mysql


def traer_usuario(email, _password):
    password = _password.encode('utf-8')
    h = hashlib.md5(password)

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `usuarios` WHERE `email` = %s AND `password` = %s AND `tipo` = %s", (email, h.hexdigest(), 0))
    data = cur.fetchall()
    cur.close()

    return data

