from flask import Flask
from flask.templating import render_template
from flask.globals import request, session
from clases.modelo import Anuncio
from operaciones_db import operaciones_db
from flask_mail import Mail, Message
import random
import string
import os
from clases.expresiones_regulares import validar_nombre, validar_precio,\
    validar_contacto
from flask import jsonify

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'pideseloasilvi@gmail.com'
app.config['MAIL_PASSWORD'] = 'tknqxsxkiiiucncd'
mail = Mail(app)

#control de sesiones:
app.secret_key = "Supercaliflagiliscoalidoso"

#Zona administrador
@app.route("/admin/")
def login():
    return render_template("admin/login_admin.html", error = "")

@app.route("/admin/<string:ruta>", methods=["POST", "GET"])   #<string:ruta> indica cualquier ruta despues de admin/. y ruta se le da a la funcion
def administracion(ruta):
    if ruta == "login":
        passwd = request.form["passwd"]   #con Post, no sirve request.args.get()
        user = request.form["user"]
        if operaciones_db.comprobar_pass(user, passwd) == 0:
            return render_template("admin/login_admin.html", error = "Contraseña o usuario erróneo")
        else:
            session["identificado"] = user   #asigno "sello" de sesión
            anuncios = operaciones_db.listar_anuncios()
            pendientes = operaciones_db.listar_anuncios_pendientes()
            return render_template("admin/listado_anuncios_admin.html", anuncios= anuncios, pendientes=pendientes)
    #comprobación si el usuario esta en sesión
    if not "identificado" in session:
        return "<a href='http://127.0.0.1:5000'>Identificate de nuevo</a>" 
         
    if ruta == "borrar":
        id_borrar = request.args["id"]
        operaciones_db.borrar_anuncio(id_borrar)  #borro el anuncio
        #borrado de la imagen correspondiente si existe, si no, pasa sin hacer nada.
        try:
            os.remove("static/img_anuncios/"+ str(id_borrar) + ".jpg")
        except:
            pass
        #se llama de nuevo a la sentencia Sql para crear las listas actualizadas
        anuncios = operaciones_db.listar_anuncios() 
        pendientes = operaciones_db.listar_anuncios_pendientes()
        return render_template("admin/listado_anuncios_admin.html", anuncios= anuncios, pendientes=pendientes)

    if ruta == "editar":
        id_editar = request.args["id"]
        anuncio = operaciones_db.obtener_anuncio_db(id_editar)
        categorias = operaciones_db.obtener_categorias()
        return render_template("admin/editar_anuncio.html", anuncio = anuncio, categorias = categorias)
    if ruta == "guardar-anuncio":
        id_guardar = request.form["id"]
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        precio = request.form["precio"].replace(",", ".")
        descripcion = request.form["descripcion"]
        envio = request.form["envio"]
        contacto = request.form["contacto"]
        if validar_nombre(nombre) and validar_precio(precio) and validar_contacto(contacto):
        #creo el nuevo objeto con los datos recibidos
            anuncio_nuevo = Anuncio(nombre, categoria, precio, descripcion, envio, contacto, id_guardar)
            operaciones_db.guardar_anuncio_editado(anuncio_nuevo)
            
            #asignamos nueva imagen en caso de que la suba
            imagen = request.files["img_file"]
            imagen.save("static/img_anuncios/" +str(id_guardar) + ".jpg")
    
            anuncios = operaciones_db.listar_anuncios() 
            pendientes = operaciones_db.listar_anuncios_pendientes()
            return render_template("admin/listado_anuncios_admin.html", anuncios= anuncios, pendientes=pendientes)
        else: 
            return render_template("admin/listado_anuncios_admin.html")
        
    if ruta == "cerrar_sesion":
        user = session["identificado"]
        session.clear()
        return render_template("admin/cierre_sesion.html", user = user)
    
    if ruta == "cerrar_sesion":
        user = session["identificado"]
        session.clear()
        return render_template("admin/cierre_sesion.html", user = user)
        
        
#Zona pública
@app.route("/")
def index():
    anuncios = operaciones_db.listar_anuncios()      #llamada a la función que lista los datos de ddbb
    return render_template("index.html", anuncios = anuncios)    #se da una variable que va a leer el index con la lista.

@app.route("/registro-anuncio")
def registrar_anuncio():
    categorias = operaciones_db.obtener_categorias()
    return render_template("registro_anuncio.html", categorias = categorias)

@app.route("/guardar-anuncio", methods=["POST"])
def guardar_anuncio():
    nombre = request.form["nombre"]
    categoria = request.form["categoria"]
    precio = request.form["precio"].replace(",", ".")
    descripcion = request.form["descripcion"]
    envio = request.form["envio"]
    contacto = request.form["contacto"]
    
    #validador de formulario: En caso de no conincidir con exp, regulares, no registra nada en ddbb
    if validar_nombre(nombre) and validar_precio(precio) and validar_contacto(contacto):
        anuncio = Anuncio(nombre, categoria, precio, descripcion, envio, contacto)   #creo objeto con datos recibidos 
        
        #genero código aleatorio para validación:
        codigo = ''.join(random.choices(string.ascii_letters + string.digits, k= 200))
       
        id_generado = operaciones_db.registrar_anuncio(anuncio, codigo)     #llamo a la función dandole el objeto, y el codigo generado
        
        #guardo el archivo de foto subido en el formulario
        imagen = request.files["img_file"]
        imagen.save("static/img_anuncios/" +str(id_generado) + ".jpg")
        
        #enviamos mail al usuario:Asunto:
        msg = Message("Gracias por registrar tu anuncio", sender ="pideseloasilvi@gmail.com", recipients=[contacto])
        #cuerpo del mensaje
        msg.html= "Muchas gracias por registrar tu anuncio con nosotros.<br/><a href='http://127.0.0.1:5000/validar-anuncio?id={}&codigo={}'>Pincha este enlace la verificar tu email</a>".format(str(id_generado), codigo)
        
        mail.send(msg)
        
        return render_template("registro_ok.html")
    else:
        return "No, no...<a href='/'>Volver Home</a>"
        

@app.route("/validar-anuncio")
def validar_anuncio():   
    id = request.args.get("id")    #obtengo los valores, de la petición de msg.html los valores
    codigo = request.args.get("codigo")
    
    resultado = operaciones_db.comprobar_codigo(id,codigo)
    if resultado ==0:    #porque en la funcion que llama a la sql no ha encontrado nada y la lista está vacia con lo que es 0
        return "Código o id no son validos id: " + str(id) + " codigo: " + str(codigo)
    if resultado ==1:
        operaciones_db.validar_email(id)
        return render_template("validacion_ok.html")

#zona chat
@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/registrar_mensaje", methods =["GET", "POST"])
def registrar_mensaje():
    nombre = request.args["nom"]
    mensaje = request.args["mesj"]
    operaciones_db.registrar_mensajes(nombre, mensaje)
    return "ok"

@app.route("/obtener_mensajes")
def obtener_mensajes_db():
    mensajes = operaciones_db.obtener_mensajes()
    return jsonify(mensajes)
    
    

app.run(debug = True)
