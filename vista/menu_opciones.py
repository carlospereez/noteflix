import ...

class MenuOpciones:
    """
    Clase que representa el menú de opciones de la aplicación.

    Esta clase muestra el menú de opciones y gestiona la opción seleccionada por el usuario.
    Proporciona métodos para mostrar el catálogo, visualizar películas y series, obtener recomendaciones, mostrar estadísticas y volver al menú de acceso.

    Attributes:
    usuario_logeado (Usuario | None): Variable que almacena el usuario que ha iniciado sesión.
    Hay dos opciones: que no se haya iniciado sesión o que en caso contrario, haya iniciado sesión un único usuario al mismo tiempo.

    Métodos:
    mostrar_menu_opciones() -> None: Muestra el menú de opciones y gestiona la opción seleccionada por el usuario.
    """

    usuario_logeado = Usuario | None = None  # variable que guarda el usuario que ha iniciado sesión

    @classmethod
    def mostrar_menu_opciones(cls):
        print("---------------------")
        print("MENU DE OPCIONES")
        print("---------------------")
        print("1. Ver catálogo")
        print("2. Visualizar película")
        print("3. Visualizar serie")
        print("4. Obtener recomendaciones")
        print("5. Mostrar estadísticas")
        print("6. Volver al menú de acceso")
        print("---------------------")
        respuesta = input("Introduzca una opción: ")
        if respuesta == "1":
            cls._mostrar_catalogo()
        if respuesta == "2":
            cls._mostrar_visualizar_media("PELICULA")
        if respuesta == "3":
            cls._mostrar_visualizar_media("SERIE")
        if respuesta == "4":
            cls._mostrar_recomendaciones()
        if respuesta == "5":
            cls._mostrar_estadisticas()
        if respuesta == "6":
            print("Volviendo al menú de acceso...")
            cls.usuario_logeado = None
            MenuAcceso.mostrar_menu_acceso()
        else:
            print("Opción inválida")
            cls.mostrar_menu_opciones()


    @classmethod
    def _mostrar_catalogo(cls):
        ...

    @classmethod
    def _mostrar_visualizar_media(cls):
        ...

    @classmethod
    def _simular_visualizacion(cls):
        ...

    @classmethod
    def _mostrar_estadisticas(cls):
        ...

    @classmethod
    def _mostrar_recomendaciones(cls):
        ...
