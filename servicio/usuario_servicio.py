from modelo import Usuario, Media, Pelicula, Serie
from typing import List
class UsuarioServicio:
    """
    ...

    """
    @classmethod
    def alta_usuario(cls, correo_electronico: str) -> None:
        """
        ...
        :param correo_electronico:
        :return:
        """

    @classmethod
    def obtener_usuario(cls, correo_electronico: str) -> Usuario:
        return UsuarioRepositorio.obtener_usuario(correo_electronico)

    @classmethod
    def obtener_usuarios(cls) -> List[Usuario]:
        return UsuarioRepositorio.obtener_usuarios()

    @classmethod
    def visualizar_media(cls, usuario: Usuario, media: Media):
        """

        :param usuario:
        :param media:
        :return:
        """
        ...
