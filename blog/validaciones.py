from blog.modelos import Autor, Post


def validar_post(post):
    if not isinstance(post, Post):
        return False, "No es un objeto Post"

    if type(post.id) != int or post.id <= 0:
        return False, "ID incorrecto"

    if type(post.titulo) != str or post.titulo.strip() == "":
        return False, "Titulo incorrecto"

    if type(post.contenido) != str or post.contenido.strip() == "":
        return False, "Contenido incorrecto"

    if not isinstance(post.autor, Autor):
        return False, "Autor incorrecto"

    if type(post.autor.nombre) != str or post.autor.nombre.strip() == "":
        return False, "Falta el nombre del autor"

    if type(post.tags) != list or len(post.tags) == 0:
        return False, "Tags incorrectos"

    for tag in post.tags:
        if type(tag) != str or tag.strip() == "":
            return False, "Tag incorrecto"

    if post.estado not in ("borrador", "publicado", "archivado"):
        return False, "Estado incorrecto"

    return True, "Valido"
