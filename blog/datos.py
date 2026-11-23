perfil_autor = {
    "nombre": "Paz",
    "bio": "Estudiante de Python",
    "especialidad": "Python",
    "redes_sociales": ["pazlindon"]
}
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Listas", "Funciones"}
posts = [
    {
        "id": 1,
        "titulo": "Aprender Python",
        "contenido": "Primeros pasos",
        "autor": perfil_autor,
        "tags": ["Python"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Funciones en Python",
        "contenido": "Uso de funciones",
        "autor": perfil_autor,
        "tags": ["Python", "Funciones"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Listas en Python",
        "contenido": "Uso de listas",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "Post incompleto",
        "autor": perfil_autor,
        "tags": ["Python"],
        "estado": "borrador"
    }
]
