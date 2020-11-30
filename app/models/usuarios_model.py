#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Este archivo ayuda a manejar la estructura lógica de los datos del usuario con la base de datos
"""

import hashlib

from app.app import mysql


def traer_usuario(email, _password):
    """

    :param email:
    :param _password:
    :return:
    """
    password = _password.encode('utf-8')
    h = hashlib.md5(password)

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `usuarios` WHERE `email` = %s AND `password` = %s", (email, h.hexdigest()))
    data = cur.fetchall()
    cur.close()

    return data


def todos_los_usuarios():
    """

    :return:
    """
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM `usuarios` WHERE `nombre` != "Admin"''')
    data = cur.fetchall()
    cur.close()

    return data


def insertar_usuario(nombre, apellidos, email, _password):
    """

    :param nombre:
    :param apellidos:
    :param email:
    :param password:
    :return:
    """
    password = _password.encode('utf-8')
    h = hashlib.md5(password)

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `usuarios`(`nombre`, `apellidos`, `email`, `tipo`, `password`) VALUES (%s,%s,%s,%s,%s)",
                (nombre, apellidos, email, 0, h.hexdigest()))
    mysql.connection.commit()
    cur.close()

    msj = "El usuario se agrego correctamente"

    return msj


def agregar_usuario(nombre, apellidos, email, _password, tipo):
    """

    :param nombre:
    :param apellidos:
    :param email:
    :param _password:
    :param tipo:
    :return:
    """

    t = '1' if tipo == 'Admin' else '0'

    password = _password.encode('utf-8')
    h = hashlib.md5(password)

    cur = mysql.connection.cursor()
    print(t)
    cur.execute("INSERT INTO `usuarios`(`nombre`, `apellidos`, `email`, `tipo`, `password`) VALUES (%s,%s,%s,%s,%s)",
                (nombre, apellidos, email, t, h.hexdigest()))
    mysql.connection.commit()
    cur.close()

    msj = "El usuario se agrego correctamente"

    return msj


def eliminar_user(user_id):
    """

    :param user_id:
    :return:
    """
    cur = mysql.connection.cursor()
    cur.execute('''DELETE FROM `usuarios` WHERE `id` = {0}'''.format(user_id))
    mysql.connection.commit()

    msj = "El usuario se eliminó correctamente"

    return msj


