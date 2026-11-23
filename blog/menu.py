def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        return int(input("Elegi una opcion: "))
    except ValueError:
        print("Ingresa un numero valido")
        return 0


def pedir_texto(mensaje):
    return input(mensaje)
