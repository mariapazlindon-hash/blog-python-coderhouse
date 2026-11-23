# Archivo principal del blog
from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            palabra = pedir_texto("Buscar titulo: ")
            buscar_por_titulo(posts, palabra)
        elif opcion == 3:
            tag = pedir_texto("Ingresa un tag: ")
            filtrar_por_tag(posts, tag)
        elif opcion == 4:
            numero = 1
            for post in posts:
                valido, mensaje = validar_post(post)
                if valido:
                    print(f"Post {numero}: valido")
                else:
                    print(f"Post {numero}: error - {mensaje}")
                numero += 1
        elif opcion == 5:
            print("Hasta luego")
            break
        elif opcion != 0:
            print("Opcion invalida")
