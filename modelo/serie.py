from media import Media
class Serie(Media):
    """
    Clase que representa una serie.

    Esta clase hereda de la clase Media y añade un atributo adicional: temporadas.
    Cada serie tiene un id, título, director, año, géneros y número de temporadas.

    Attributes:
    id (int): El identificador único de la serie.
    titulo (str): El título de la serie.
    director (str): El director de la serie.
    anio (int): El año de lanzamiento de la serie.
    generos (list of str): La lista de géneros de la serie.
    temporadas (int): El número de temporadas de la serie.
    """
    def __init__(self, id, titulo, director, anio, generos, temporadas):
        """
        Inicializa un objeto de la clase Serie.

        Parámetros:
        id (int): El identificador único de la serie.
        titulo (str): El título de la serie.
        director (str): El director de la serie.
        anio (int): El año de lanzamiento de la serie.
        generos (list of str): La lista de géneros de la serie.
        temporadas (int): El número de temporadas de la serie.
        """
        super().__init__(id, titulo, director, anio, generos)
        self.temporadas = temporadas

