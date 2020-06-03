from AutoTest.models import Test, Usuario

from django.shortcuts import render
import sqlite3

#metodo devuelve una conexion para la base de datos
def conectar():
    cn = sqlite3.connect("db.sqlite3")
    return cn
#metodo cierra la conexion con la BD
def desconectar(cn):
    cn.close()

#metodo recoge  el ultimo id insertado
def recoger_ultimo_Usuario():
    cn = conectar()
    cursor = cn.cursor()

    query_select = "SELECT MAX(id) FROM AutoTest_usuario"
    cursor.execute(query_select)
    ultimo_id = cursor.fetchone()

    desconectar(cn)

    return ultimo_id
#metodo que inserta un usuario
def insertar_Usuario(usu):
    cn = conectar()
    cursor = cn.cursor()

    usu_attr = vars(usu)

    if usu_attr["telefono"] == "":
        query_insert = "INSERT INTO AutoTest_usuario (edad, sexo, cp) VALUES ("  \
            + usu_attr["edad"] + ", " \
            + "'" + usu_attr["sexo"] + "', " \
            + "'" + usu_attr["cp"] + "')"
    else:
        query_insert = "INSERT INTO AutoTest_usuario (edad, sexo, cp, telefono) VALUES ("  \
            + usu_attr["edad"] + ", " \
            + "'" + usu_attr["sexo"] + "', " \
            + "'" + usu_attr["cp"] + "', " \
            + "'" + usu_attr["telefono"] + "')"

    cursor.execute(query_insert)
    cn.commit()

    desconectar(cn)

#metodo que inserta el test
def insertar_Test(test):
    cn = conectar()
    cursor = cn.cursor()

    test_attr =  vars(test)
    usuario_id = recoger_ultimo_Usuario()[0]

    query_insert = "INSERT INTO AutoTest_test (fiebre, tos_seca, asfixia, perdida_sentidos, repentino, resultado, usuario_id) VALUES ("  \
        + str(test_attr["fiebre"]) + ", " \
        + str(test_attr["tos_seca"]) + ", " \
        + str(test_attr["asfixia"]) + ", " \
        + str(test_attr["perdida_sentidos"]) + ", " \
        + str(test_attr["repentino"]) + ", " \
        + str(test_attr["resultado"]) + ", " \
        + str(usuario_id) + ")"

    cursor.execute(query_insert)
    cn.commit()

    desconectar(cn)