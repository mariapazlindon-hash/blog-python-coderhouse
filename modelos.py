from blog.operaciones import mostrar_posts


class Autor:
    def __init__(self, nombre, bio, especialidad, redes_sociales):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }


class Blog:
    def __init__(self, posts):
        self.posts = posts

    def listar_posts(self):
        mostrar_posts(self.posts)

    def buscar_por_titulo(self, termino):
        if termino.strip() == "":
            print("La busqueda esta vacia")
            return

        resultados = []
        for post in self.posts:
            if termino.lower() in post.titulo.lower():
                resultados.append(post)
        mostrar_posts(resultados)

    def filtrar_por_tag(self, tag):
        if tag.strip() == "":
            print("El tag esta vacio")
            return

        resultados = []
        for post in self.posts:
            for etiqueta in post.tags:
                if etiqueta.lower() == tag.lower():
                    resultados.append(post)
                    break
        mostrar_posts(resultados)

    def crear_post(self, post):
        self.posts.append(post)
