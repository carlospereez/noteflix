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
        ...

    @classmethod
    def _mostrar_catalogo(cls):
        ...

    @classmethod
    def _mostrar_visualizar_media(cls):
        ...

    @classmethod
    def _simular_visualización(cls):
        ...

    @classmethod
    def _mostrar_estadisticas(cls):
        ...

    @classmethod
    def _mostrar_recomendaciones(cls):
        ...
