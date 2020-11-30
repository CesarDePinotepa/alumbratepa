#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Este archivo maneja las interacciones con la tabla de reportes de la base de datos
"""

import datetime
from random import seed, randint

from app.app import mysql


def traer_todos_los_reportes():
    """
    Esta funcion ayuda a traer todos los reportes desde la base de datos
    """
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM `reporte`''')
    data = cur.fetchall()
    cur.close()

    return data


def traer_reportes_por_usuario(uid):
    """

    :param uid:
    :return:
    """
    user_id = str(uid)
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM `reporte` WHERE `user_id` = %s''', user_id)
    data = cur.fetchall()
    cur.close()

    return data


def insertar_reporte(select, direccion, comentario, user_id, poste):
    """

    :param select:
    :param direccion:
    :param comentario:
    :param user_id:
    :param poste:
    :return:
    """
    fecha = datetime.date.today()
    status = "Activo"

    a = datetime.datetime.now()
    r_num = a.strftime("%S")
    num_reporte = "AP-"+str(fecha)+str(r_num)

    print(num_reporte, "-", select, "-", direccion, "-", comentario, "-", user_id, "-", poste, "-", fecha)

    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO `reporte`(`numero_reporte`, `direccion`, `status`, `fecha`, `poste`, '''
                '''`funcionamiento`, `comentario`, `user_id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
                (num_reporte, direccion, status, fecha, poste, select, comentario, user_id))
    mysql.connection.commit()

    msj = "El reporte se realizó correctamente"

    return msj

