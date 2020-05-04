import re
exp_nombre = "^[a-zA-Z0-9 ñNÁÉÍÓÚáéíó]{4,40}$"

exp_precio = "^[0-9,]+(.[0-9]{2})?$"

exp_contacto = "^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,5}$"

def validar_nombre(nombre):
    validador_nombre = re.compile(exp_nombre)
    return validador_nombre.match(nombre)

def validar_precio(precio):
    validador_precio = re.compile(exp_precio)
    return validador_precio.match(precio)

def validar_contacto(contacto):
    validador_contacto = re.compile(exp_contacto)
    return validador_contacto.match(contacto)
    
    
    

    
    
    