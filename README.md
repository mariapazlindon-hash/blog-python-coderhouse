# Preentrega 6 - Sistema de Blog
**Autora:** Paz Lindon
## Descripcion
Sistema de blog desarrollado en Python.
En esta entrega se agregaron clases y guardado de posts en JSON.
## Funcionalidades
- Ver todos los posts.
- Buscar posts por titulo.
- Filtrar por etiquetas.
- Crear nuevos posts.
- Validar publicaciones.
- Guardar y cargar posts en JSON.
- Salir del programa.
## Clases
- Autor: guarda los datos del autor.
- Post: representa una publicacion.
- Blog: administra las publicaciones.
## Organizacion del proyecto
- main.py: ejecuta el programa.
- blog/modelos.py: contiene las clases.
- blog/datos.py: carga y guarda los posts en JSON.
- blog/menu.py: muestra el menu.
- blog/operaciones.py: contiene las operaciones del blog.
- blog/validaciones.py: valida las publicaciones.
- blog/__init__.py: identifica el paquete.
- posts.json: guarda las publicaciones.
## Como ejecutar
1. Abrir la carpeta del proyecto en VS Code.
2. Abrir la terminal.
3. Ejecutar:
python3 main.py
## Guardado de datos
Al iniciar, el programa carga los posts desde posts.json.
Al elegir la opcion 6, guarda las publicaciones en ese archivo.
Los datos se convierten de objetos a diccionarios para guardarlos y se reconstruyen como objetos al cargarlos.
## Cambios respecto a la Preentrega 5
Se agregaron las clases Autor, Post y Blog.
Tambien se incorporo la creacion de posts y la persistencia en JSON.
