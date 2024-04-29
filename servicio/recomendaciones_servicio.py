from typing import List

from modelo import Usuario, Media
class RecomendacionesServicio:
    @classmethod
    def obtener_recomendaciones(cls, usuario: Usuario) -> List[Media]:
        ...
