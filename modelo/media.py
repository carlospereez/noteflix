from abc import ABC
class Media(ABC):
    """
    Clase abstracta que representa un contenido multimedia.

    Esta clase sirve como base para otras clases que representan tipos específicos de contenido multimedia,
    como películas o series. Cada contenido multimedia tiene un id, título, director, año y géneros.

    Attributes:
    id (int): El identificador único del contenido multimedia.
    titulo (str): El título del contenido multimedia.
    director (str): El director del contenido multimedia.
    anio (int): El año de lanzamiento del contenido multimedia.
    generos (list of str): La lista de géneros del contenido multimedia.
    """

    def __init__(self, id, titulo, director, anio, generos):
        """
        Inicializa un objeto de la clase Media.

        Parámetros:
        id (int): El identificador único del contenido multimedia.
        titulo (str): El título del contenido multimedia.
        director (str): El director del contenido multimedia.
        anio (int): El año de lanzamiento del contenido multimedia.
        generos (list of str): La lista de géneros del contenido multimedia.
        """
        self.id = id
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.generos = generos


