from .media import Media
class Pelicula(Media):
    """
    Clase que representa una película.

    Esta clase hereda de la clase Media y añade un atributo adicional: duracion.
    Cada película tiene un id, título, director, año, géneros y duración.

    Attributes:
    id (int): El identificador único del pelicula.
    titulo (str): El título de la película.
    director (str): El director de la película.
    anio (int): El año de lanzamiento de la película.
    generos (list of str): La lista de géneros de la película.
    duracion (int): La duración de la película en minutos.
    """
    def __init__(self, id, titulo, director, anio, generos, duracion):
        """
        Inicializa un objeto de la clase película.

        Parameters:
        id (int): El identificador único de la película.
        titulo (str): El título de la película.
        director (str): El director de la película.
        anio (int): El año de lanzamiento de la película.
        generos (list of str): La lista de géneros de la película.
        duracion (int): La duración de la película en minutos.
        """
        super().__init__(id,titulo,director,anio,generos)
        self.duracion = duracion

    def __str__(self):
        """
        Devuelve una representación en cadena de la película preparado para
        mostrarse tabulado en la terminal.

        Returns:
        str: Una cadena que representa la película.
        """
        return f'{self.id}\t{self.titulo}\t{self.director}\t{self.anio}\t{self.duracion}\t{", ".join(self.generos)}'
