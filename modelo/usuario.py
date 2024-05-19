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

    def __init__(self, correo_electronico: str, peliculas_vistas: List[Pelicula], series_vistas: List[Serie]):
        """
        Inicializa un objeto de la clase Usuario.

        Parámetros:
        correo_electronico (str): El correo electrónico del usuario.
        peliculas_vistas (list of Pelicula): La lista de películas que el usuario ha visto.
        series_vistas (list of Serie): La lista de series que el usuario ha visto.
        """
        self.correo_electronico = correo_electronico
        self.peliculas_vistas = peliculas_vistas
        self.series_vistas = series_vistas

    def __str__(self):
        """
        Devuelve una representación en cadena del usuario, tabulado para mostrarse en terminal.

        Returns:
        str: Una cadena que representa al usuario.
        """
        return f'{self.correo_electronico}\t{len(self.peliculas_vistas)}\t{len(self.series_vistas)}'