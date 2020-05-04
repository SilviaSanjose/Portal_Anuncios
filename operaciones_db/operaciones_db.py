import mysql.connector
from operaciones_db import constantes_db
from clases import modelo

def conectar():
    my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "db_anuncios_manualidades"
    )
    return my_db

def registrar_anuncio(anuncio, codigo):
    sql = constantes_db.SQL_REGISTRO_ANUNCIO
    my_db = conectar()
    id_generado = -1     #creamos la variable con -1 ya que los id en base de datos siempre son positivos
    try:
        cursor = my_db.cursor()
        val = (anuncio.nombre, anuncio.categoria, anuncio.precio, anuncio.descripcion, anuncio.envio, anuncio.contacto, codigo)
        cursor.execute(sql,val)
        my_db.commit()
        id_generado = cursor.lastrowid     #que id_generado recoja el ultimo id que se ha dado en base de datos con el nuevo registro.
    except Exception as e:
        print(e)
    finally:
        if my_db is not None:
            my_db.disconnect()
    return id_generado

def listar_anuncios():
    sql = constantes_db.SQL_LISTAR_ANUNCIO
    my_db = conectar()
    lista = ""
    try:
        cursor = my_db.cursor()
        cursor.execute(sql)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if my_db is not None:
            my_db.disconnect()
    return lista     

def comprobar_codigo(id, codigo):
    sql = constantes_db.SQL_COMPROBAR_CODIGO
    my_db = conectar()
    lista = ""
    try:
        cursor = my_db.cursor()
        val = (id, codigo)
        cursor.execute(sql, val)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if my_db is not None:
            my_db.disconnect()
    return len(lista)   #si da 0 es porque id y codigo no son validos, con lo cual no devuelve nada, si encuentra id y codigo, devuelve 1

def validar_email(id):
    sql = constantes_db.SQL_VALIDAR_EMAIL
    my_db = conectar()
    cursor = my_db.cursor()
    val = (id,)
    cursor.execute(sql, val)
    my_db.commit()
    my_db.disconnect()
    
def obtener_categorias():
    sql = constantes_db.SQL_OBTENER_CATEGORIAS
    my_db = conectar()
    cursor = my_db.cursor()
    cursor.execute(sql)
    lista_cat = cursor.fetchall()
    my_db.disconnect()
    return lista_cat


#Zona Admin 
def listar_anuncios_pendientes():
    sql = constantes_db.SQL_LISTAR_ANUNCIO_PENDIENTE
    my_db = conectar()
    lista = ""
    try:
        cursor = my_db.cursor()
        cursor.execute(sql)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if my_db is not None:
            my_db.disconnect()
    return lista 
  
def borrar_anuncio(id_borrar):
    sql = constantes_db.SQL_BORRAR_ANUNCIO
    my_db = conectar()
    cursor = my_db.cursor()
    val = (id_borrar,)
    cursor.execute(sql, val)
    my_db.commit()
    my_db.disconnect()
 
def obtener_anuncio_db(id_obtener):
    sql = constantes_db.SQL_OBTENER_ANUNCIO_DB
    my_db = conectar()
    cursor = my_db.cursor()
    val = (id_obtener,)
    cursor.execute(sql, val)
    lista = cursor.fetchone() 
    my_db.disconnect()
    anuncio = modelo.Anuncio(num_id = lista[0], nombre = lista[1], categoria = lista[2], precio = lista[3], descripcion = lista[4], envio = lista[5], contacto = lista[6] )
    return anuncio

def guardar_anuncio_editado(anuncio):
    sql = constantes_db.SQL_GUARDAR_ANUNCIO_EDITADO
    my_db = conectar()
    cursor = my_db.cursor()
    val = (anuncio.nombre, anuncio.categoria, anuncio.precio, anuncio.descripcion, anuncio.envio, anuncio.contacto, anuncio.num_id)
    cursor.execute(sql, val)
    my_db.commit()
    my_db.disconnect()

#comprobación usuario
def comprobar_pass(user, passwd):
    sql = constantes_db.SQL_COMPORBAR_USUARIO
    my_db = conectar()
    cursor = my_db.cursor()
    val = (user, passwd)
    cursor.execute(sql, val)
    res = cursor.fetchall()
    my_db.disconnect()
    return len(res)
    
#CHAT
def registrar_mensajes(nombre, mensaje):
    sql = constantes_db.SQL_REGISTRAR_MENSAJES
    my_db = conectar()
    cursor = my_db.cursor()
    val = (nombre, mensaje)
    cursor.execute(sql,val)
    my_db.commit()
    my_db.disconnect()
    
    
def obtener_mensajes():
    sql = constantes_db.SQL_OBTENER_MENSAJES
    my_db = conectar()
    cursor = my_db.cursor()
    cursor.execute(sql)
    mensajes = cursor.fetchall()
    my_db.disconnect()
    return mensajes
    
    

    