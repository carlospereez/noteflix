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
            pass
        elif respuesta == 2:
            pass
        elif respuesta == 3:
            pass
        elif respuesta == 4:
            print("saliendo...")
            exit()
        else:
            print("Opción válida")
            cls.mostrar_menu_acceso()

    @classmethod
    def alta_usuario(cls):
        mail = input("Introduzca el mail a registrar:")
        try:
            UsuarioServicio.alta_usuario(mail)
        except(Exception):  # "UsuarioyaexisteError"
            print("El usuario ya está registrado")
        except(Exception):  # "MailInvalidoError"
            print("El texto introducido no es un mail")
        finally:
            cls.login()

    @classmethod
    def login(cls):
        usuario = input("Introduzca el nombre de usuario")
        try:
            cls.usuario_logeado = UsuarioServicio.comprobar_usuario(usuario)
            cls.mostrar_menu_opciones()
        except:  # aclarar tipos de errores
            print("El usuario no existe")
            cls.mostrar_menu_acceso()


    @classmethod
    def mostrar_menu_opciones(cls):
        print("1. Ver catálogo")
        print("2. Visualizar película")
        print("3. Obtener recomendaciones")
        print("4. Mostrar estadísticas")
        print("5. Volver al menú de acceso")
        respuesta = input("Introduzca una opción")
        if respuesta == "1":
            # Función para mostrar...
        elif(respuesta == "2"):
            ...
        elif(respuesta == "3"):
            cls.obtener_recomendaciones()
        elif(respuesta == "4"):
            cls.mostrar_estadísticas()
        elif(respuesta == "5"):
            cls.usuario_logeado = None
            print("Volviendo al menú de acceso")
            cls.mostrar_menu_acceso()
        else:
            print("Opcion invalida")
            cls.mostrar_menu_opciones()

    @classmethod
    def mostras_estadísticas(cls):
        print("Generando gráfico de estadísticas del usario "+ cls.usuario_logeado.mail)
        EstadisticasServicio.obtener_estadisticas_usuarios(cls.usuario_logeado)