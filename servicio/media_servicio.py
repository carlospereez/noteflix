from typing import List

from modelo import Pelicula, Serie, Media, Usuario
from modelo.repositorio.media_repositorio import MediaRepositorio


class MediaServicio:
    """
      Clase que representa el servicio de contenido multimedia.

      Esta clase se encarga de la gestión de las películas y series haciendo uso del repositorio, incluyendo la obtención de una película o serie por su identificador,
      y la obtención de listados de todas las películas y series.

      Methods:
      obtener_pelicula_por_id(id_pelicula: str) -> Pelicula | None: Devuelve una película por su identificador
      obtener_serie_por_id(id_serie: str) -> Serie | None: Devuelve una serie por su identificador
      obtener_listado_peliculas() -> List[Pelicula]: Devuelve una lista de todas las películas
      obtener_listado_series() -> List[Serie]: Devuelve una lista de todas las series
      """

    @classmethod
    def obtener_pelicula_por_id(cls, id_pelicula: str) -> Pelicula | None:
        return MediaRepositorio.obtener_pelicula_por_id(id_pelicula)

    @classmethod
    def obtener_serie_por_id(cls, id_serie: str) -> Serie | None:
        return MediaRepositorio.obtener_serie_por_id(id_serie)

    @classmethod
    def obtener_listado_peliculas(cls) -> List[Pelicula]:
        return MediaRepositorio.obtener_peliculas()

    @classmethod
    def obtener_listado_series(cls) -> List[Serie]:
        return MediaRepositorio.obtener_series()