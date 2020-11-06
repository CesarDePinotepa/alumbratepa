#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Este archivo maneja las interacciones con la tabla de reportes de la base de datos
"""

from datetime import datetime
from random import seed, randint

from app.app import mysql


def traer_todos_los_reportes():
    """
    Esta funcion ayuda a traer todos los reportes desde la base de datos
    """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM `reporte` ')
    data = cur.fetchall()
    cur.close()

    return data


def traer_reportes_por_usuario(user_id):
    """

    :param user_id:
    :return:
    """

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM `reporte` WHERE `user_id` = %s', user_id)
    data = cur.fetchall()
    cur.close()

    return data


def insertar_reporte(select, direccion, comentario, user_id):
    """

    :param select:
    :param direccion:
    :param comentario:
    :param user_id:
    :return:
    """
    fecha = datetime.now()
    status = "Activo"

    seed(1)
    r_num = [randint(0, 1000) in range(1000)]

    num_reporte = "AP-"+str(fecha)+str(r_num)

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `reporte`(`numero_reporte`, `direccion`, `status`, `fecha`, `poste`, "
                "`funcionamiento`, `comentario`, `user_id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (num_reporte, direccion, status, fecha, r_num, select, comentario, user_id))
    mysql.connection.commit()

    return True

