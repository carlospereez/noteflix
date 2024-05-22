import time
from multiprocessing import Process
from modelo import media, Usuario
from servicio import RecomendacionesServicio, EstadisticasServicio, UsuarioServicio, MediaServicio
from vista import MenuAcceso


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

    usuario_logeado: Usuario | None = None  # variable que guarda el usuario que ha iniciado sesión

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

    @classmethod  # CAMBIAR Y HACERLO EN CSV ANTES DE LA ENTREGA
    def _mostrar_catalogo(cls):
        print("---------------------------")
        print("Peliculas:")
        print("---------------------------")
        print("ID\tTítulo\tDirector\tAño\tDuración\tGéneros")
        [print(pelicula) for pelicula in MediaServicio.obtener_listado_peliculas()]
        print("---------------------------")
        print("Series:")
        print("---------------------------")
        print("ID\tTítulo\tDirector\tAño\tTemporadas\tGéneros")
        [print(serie) for serie in MediaServicio.obtener_listado_series()]
        print("---------------------------")
        print("Pulse ENTER para continuar...")
        input()
        cls.mostrar_menu_opciones()

    @classmethod
    def _mostrar_visualizar_media(cls, tipo_media: str):
        if tipo_media == "PELICULA":
            id_media = input("Introduzca el id de la película a visualizar")
        elif tipo_media == "SERIE":
            id_media = input("Introduzca el id de la serie a visualizar")
        else:
            # Si la funcion no recibe un tipo de media válido, se muestra un mensaje de error, gestionado por una excepción
            raise Exception("Tipo de media no válido")

        media = MediaServicio.obtener_pelicula_por_id(
            id_media) if tipo_media == "PELICULA" else MediaServicio.obtener_serie_por_id(id_media)
        if media is None:
            print("No se encontró el media con el id indicado")
            print("Volviendo al menú de opciones...")
            cls.mostrar_menu_opciones()
        else:
            print("Se va a visualizar: " + media.titulo)
            respuesta = input("Es correcto? (s/n):")
            if respuesta == "s":
                cls._simular_visualizacion(media)
            else:
                print("Volviendo al menú de opciones...")
                cls.mostrar_menu_opciones()


    @classmethod
    def _simular_visualizacion(cls):
        """
        Simula la visualización de una película o serie.

        Este método inicia un procso hijo que simula la visualización de la película
        o serie seleccionada. Muestra un mensaje de visualización cada segundo mientras el proceso hijo
        está vivo. Una vez que el proceso hijo termina, actualiza el usuario logeado
        con las actualizaciones realizadas.
        """

        proceso_hijo = Process(target=UsuarioServicio.visualizar_media, args=(
            cls.usuario_logeado, media))  # Creamos un proceso hijo que va a lanzar la funcion de visualizar_media
        proceso_hijo.start()  # Iniciamos el proceso hijo que simula la visualización de la pelicula

        print(f"Visualizando {media.titulo}...", end="")
        while proceso_hijo.is_alive():  # Mientras el proceso hijo esté vivo, mostramos un mensaje de visualización cada segundo
            print(".", end="")
            time.sleep(1)
        proceso_hijo.join()  # Esperamos a que el proceso hijo termine de ejecutarse
        print("\nVisualización finalizada")
        print("Pulse ENTER para continuar...")
        input()
        cls.usuario_logeado = UsuarioServicio.obtener_usuario(
            cls.usuario_logeado.correo_electronico)  # Actualizamos el usuario logeado con las actualizaciones realizadas

        cls.mostrar_menu_opciones()

    @classmethod
    def _mostrar_estadisticas(cls):
        print("Generando gráfico de estadísticas del usuario " + cls.usuario_logeado.correo_electronico)
        estadisticas_peliculas, estadisticas_series = EstadisticasServicio.obtener_estadisticas(cls.usuario_logeado)

        print("---------------------")
        print("Estadísticas de películas vistas: ")
        print("---------------------")
        print("Genero\tPeliculas vistas")
        for estadistica in estadisticas_peliculas:
            print(f'{estadistica}\t{estadisticas_peliculas[estadistica]}')

        print("---------------------")
        print("Estadísticas de series vistas: ")
        print("---------------------")
        print("Genero\tSeries vistas")
        for estadistica in estadisticas_series:
            print(f'{estadistica}\t{estadisticas_series[estadistica]}')

    @classmethod
    def _mostrar_recomendaciones(cls):  # HACER EN CSV ANTES DE ENVIARLO
        print("Generando recomendaciones para el usuario " + cls.usuario_logeado.correo_electronico)
        peliculas_recomendadas, series_recomendadas = RecomendacionesServicio.obtener_recomendaciones(
            cls.usuario_logeado)

        print("---------------------")
        print("Peliculas Recomendadas: ")
        print("---------------------")
        print("ID\tTítulo\tDirector\tAño\tDuración\tGéneros")
        [print(pelicula) for pelicula in peliculas_recomendadas]

        print("---------------------------")
        print("Series recomendadas:")
        print("---------------------------")
        print("ID\tTítulo\tDirector\tAño\tTemporadas\tGéneros")
        [print(serie) for serie in series_recomendadas]

        print("Pulse ENTER para continuar...")
        input()
        cls.mostrar_menu_opciones()
