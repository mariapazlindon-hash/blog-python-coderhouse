import json
from blog.modelos import Autor, Post
from blog.validaciones import validar_post


# Cargar los datos guardados al iniciar el programa.
def cargar_posts():
    try:
        with open("posts.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("No existe posts.json. El blog comienza vacio.")
        return []
    except json.JSONDecodeError:
        print("posts.json esta vacio o tiene un formato incorrecto.")
        return []
    except OSError:
        print("No se pudo leer posts.json.")
        return []

    if type(datos) != list:
        print("Error: posts.json debe contener una lista.")
        return []

    posts = []
    for dato in datos:
        try:
            autor_datos = dato["autor"]
            autor = Autor(
                autor_datos["nombre"],
                autor_datos.get("bio", ""),
                autor_datos.get("especialidad", "Python"),
                autor_datos.get("redes_sociales", [])
            )
            post = Post(
                dato["id"], dato["titulo"], dato["contenido"],
                autor, dato["tags"], dato["estado"]
            )
            valido, mensaje = validar_post(post)
            if valido:
                posts.append(post)
            else:
                print("Se omitio un post:", mensaje)
        except (KeyError, TypeError, AttributeError):
            print("Se omitio un post con datos incompletos.")

    return posts


# Convertir objetos a diccionarios y guardarlos en JSON.
def guardar_posts(posts):
    try:
        datos = []
        for post in posts:
            datos.append(post.to_dict())

        with open("posts.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print("Posts guardados correctamente.")
    except (OSError, TypeError, AttributeError, ValueError):
        print("Error: no se pudieron guardar los posts.")
