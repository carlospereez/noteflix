from __future__ import annotations

from servicio import UsuarioServicio

class MenuAcceso:

    usuario_logeado = None
    @classmethod
    def mostrar_menu_acceso(cls):
        print("-------------")  #ajustar estilo
        print("Bienvenido....")
        print("1. Dar usuario de alta")
        print("2. Acceder")
        respuesta = input("Escoja una opción:")
        if respuesta == "1":
            cls.alta_usuario()
        elif respuesta == "2":
            cls.mostrar_menu_opciones()
        else:
            print("Opción inválida")
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