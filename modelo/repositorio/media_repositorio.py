from typing import List
from modelo import Pelicula
from modelo.serie import Serie


class MediaRepositorio:
    @classmethod
    def getPeliculas(cls) -> List[Pelicula]:
        pass

    @classmethod
    def getSeries(cls) -> List[Serie]:
        pass