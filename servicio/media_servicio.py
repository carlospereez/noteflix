from typing import List

from modelo import Pelicula, Serie, Media, Usuario
class MediaServicio:
    @classmethod
    def obtener_listado_peliculas(cls) -> List[Pelicula]:
        ...

    @classmethod
    def obtener_listado_series(cls) -> List[Serie]:
        ...

    @classmethod
    def visualizar_media(cls, usuario: Usuario, media: Media):
        ...
