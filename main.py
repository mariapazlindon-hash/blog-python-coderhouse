from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu, pedir_texto
from blog.modelos import Autor, Post, Blog
from blog.validaciones import validar_post


if __name__ == "__main__":
    mi_blog = Blog(cargar_posts())

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            mi_blog.listar_posts()

        elif opcion == 2:
            palabra = pedir_texto("Buscar titulo: ")
            mi_blog.buscar_por_titulo(palabra)

        elif opcion == 3:
            tag = pedir_texto("Ingresar tag: ")
            mi_blog.filtrar_por_tag(tag)

        elif opcion == 4:
            titulo = pedir_texto("Titulo: ")
            contenido = pedir_texto("Contenido: ")
            tag = pedir_texto("Tag: ")

            if titulo == "" or contenido == "" or tag == "":
                print("Error: no puede haber campos vacios")
            else:
                nuevo_id = 1
                for post in mi_blog.posts:
                    if post.id >= nuevo_id:
                        nuevo_id = post.id + 1

                autor = Autor("Paz", "Estudiante de Python", "Python", ["pazlindon"])
                nuevo_post = Post(nuevo_id, titulo, contenido, autor, [tag], "publicado")
                valido, mensaje = validar_post(nuevo_post)

                if valido:
                    mi_blog.crear_post(nuevo_post)
                    print("Post creado. Usa la opcion 6 para guardarlo.")
                else:
                    print("Error:", mensaje)

        elif opcion == 5:
            numero = 1
            for post in mi_blog.posts:
                valido, mensaje = validar_post(post)
                print(f"Post {numero}: {mensaje}")
                numero += 1

        elif opcion == 6:
            guardar_posts(mi_blog.posts)

        elif opcion == 7:
            print("Hasta luego")
            break

        elif opcion != 0:
            print("Opcion invalida")
