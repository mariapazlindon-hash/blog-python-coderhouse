# Reglas para validar los posts
from blog.datos import estados_post
def validar_post(post):
    if type(post) != dict:
        return False, "No es un diccionario"
    claves = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves:
        if clave not in post:
            return False, "Falta " + clave
    if type(post["titulo"]) != str or post["titulo"].strip() == "":
        return False, "Titulo incorrecto"
    if type(post["contenido"]) != str or post["contenido"].strip() == "":
        return False, "Contenido incorrecto"
    if type(post["autor"]) != dict:
        return False, "Autor incorrecto"
    nombre = post["autor"].get("nombre", "")
    if type(nombre) != str or nombre.strip() == "":
        return False, "Falta nombre del autor"
    if type(post["tags"]) != list:
        return False, "Tags incorrectos"
    if post["estado"] not in estados_post:
        return False, "Estado incorrecto"
    return True, "Valido"