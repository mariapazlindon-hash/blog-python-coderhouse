# Operaciones del blog
def listar_posts(lista):
    for post in lista:
        if type(post) == dict:
            autor = post.get("autor", {})
            if type(autor) != dict:
                autor = {}
            print(
                post.get("titulo", "Sin titulo"),
                "| Autor:",
                autor.get("nombre", "Sin autor"),
                "| Estado:",
                post.get("estado", "Sin estado")
            )
        else:
            print("Post incorrecto")

def buscar_por_titulo(lista, termino):
    if termino.strip() == "":
        print("La busqueda esta vacia")
        return
    encontrado = False
    for post in lista:
        if type(post) == dict:
            titulo = post.get("titulo", "")
            if type(titulo) == str and termino.lower() in titulo.lower():
                print(titulo)
                encontrado = True
    if not encontrado:
        print("No se encontraron posts")
def filtrar_por_tag(lista, tag):
    if tag.strip() == "":
        print("El tag esta vacio")
        return
    encontrado = False
    for post in lista:
        if type(post) == dict and type(post.get("tags")) == list:
            for etiqueta in post["tags"]:
                if type(etiqueta) == str and etiqueta.lower() == tag.lower():
                    print(post.get("titulo", "Sin titulo"))
                    encontrado = True
                    break
    if not encontrado:
        print("No se encontraron posts")
