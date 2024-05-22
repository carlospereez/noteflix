from __future__ import annotations

from servicio import UsuarioServicio

class MenuAcceso:
    """
    Clase que representa el menú de acceso de la aplicación.

    Esta clase se encarga de mostrar el menú de acceso y gestionar las opciones seleccionadas por el usuario.
    Proporciona métodos para dar de alta a un usuario, acceder con un usuario existente, listar todos los usuarios y salir de la aplicación.

    Métodos:
    mostrar_menu_acceso() -> None: Muestra el menú de acceso y gestiona las opciones seleccionadas por el usuario.
    """

    @classmethod
    def mostrar_menu_acceso(cls):
        cls.usuario_logueado = None
        print("---------------------------")
        print("Menú de acceso")
        print("---------------------------")
        print("1. Dar usuario de alta")
        print("2. Acceder")
        print("3. Listado de usuarios")
        print("4. Salir")
        print("---------------------------")
        respuesta = input("Escoja una opción")
        if respuesta == 1:
            cls._alta_usuario()
        elif respuesta == 2:
            cls._acceder()
        elif respuesta == 3:
            cls._listar_usuarios()
        elif respuesta == 4:
            print("saliendo...")
            exit()
        else:
            print("Opción válida")
            cls.mostrar_menu_acceso()

    @classmethod
    def _alta_usuario(cls):
        mail = input("Introduzca el mail a registrar:")
        try:
            UsuarioServicio.alta_usuario(mail)
            print("Se ha registrado al usuario correctamente: " + mail)
        except Exception as e:  # "UsuarioyaexisteError..."
            print(e)
        finally:
            cls.mostrar_menu_acceso()

    @classmethod
    def _acceder(cls):
        from .menu_opciones import MenuOpciones
        usuario = input("Introduzca el mail de usuario: ")
        try:
            MenuOpciones.usuario_logeado = UsuarioServicio.obtener_usuario(usuario)
            print("Bienvenido " + MenuOpciones.usuario_logeado.correo_electronico)
        except:  # aclarar tipos de errores...
            print("El usuario no existe")
            cls.mostrar_menu_acceso()
        MenuOpciones.mostrar_menu_opciones()

    @classmethod
    def _listar_usuarios(cls):
        usuarios = UsuarioServicio.obtener_usuarios()
        if len(usuarios) == 0:
            print("No hay usuarios registrados aún")
            cls.mostrar_menu_acceso()
        else:
            print("---------------------------")
            print("Usuarios:")
            print("---------------------------")
            print("Correo electrónico\tPeliculas vistas\tSeries vistas")
            [print(usuario) for usuario in usuarios]
            print("---------------------------")
            print("Pulse ENTER para continuar...")
            input()
            cls.mostrar_menu_acceso()