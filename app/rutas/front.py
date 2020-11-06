# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# """
# Este archivo ayuda a enrutar los archivos de las vistas (archivos html) de la aplicación
# """
#
# from flask import Blueprint
#
# from app.controladores.homecontroller import homecontroller
#
# front = Blueprint("front", __name__)
#
#
# @front.route('/', methods=['GET'])
# def home():
#     return homecontroller.index()
#
#
# @front.route('/registro', methods=['GET'])
# def registrar():
#     return homecontroller.registro()
#
#
# @front.route('/registro', methods=['POST'])
# def registrar_usuario():
#     return homecontroller.registro_usuario()
#
#
# @front.route('/login', methods=['GET'])
# def login():
#     return homecontroller.login()
#
#
# @front.route('/login', methods=['POST'])
# def iniciar_sesion():
#     return homecontroller.iniciar_sesion()
#
#
# @front.route('/inicio', methods=['GET'])
# def ver_inicio():
#     return homecontroller.ver_inicio_sesion()
#
