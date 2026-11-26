# Funcion de apoyo para mostrar publicaciones.
def mostrar_posts(lista):
    if len(lista) == 0:
        print("No se encontraron posts")

    for post in lista:
        print(f"- {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")
