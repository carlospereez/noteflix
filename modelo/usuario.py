from typing import List

from modelo import Pelicula, Serie

class Usuario:
    """
    Clase que representa a un usuario.

    Cada usuario tiene asociado un correo electrónico y una lista de series y películas que ha visualizado.

    Atributos:
    · correo-electronico (str): Este es el correo electrónico del usuario.
    · peliculas-vistas (list of Pelicula) : La lista de películas que el usuario ha visualizado.
    · series-vistas (list of Series): La lista de series que el usuario ha visualizado.
    """

    def __init__(self, correo_electronico: str, peliculas_vistas: List[Pelicula], series_vistas, List[Serie]):
    """
    Inicializa un objeto de la clase Usuario.

    Parámetros:
    correo_electronico (str): El correo electrónico del usuario.
    peliculas_vistas (list of Pelicula): La lista de películas que el usuario ha visto.
    series_vistas (list of Serie): La lista de series que el usuario ha visto.
    """