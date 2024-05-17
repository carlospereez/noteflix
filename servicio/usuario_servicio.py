from modelo import Usuario, Media, Pelicula, Serie
from typing import List
import time
import re
from modelo.repositorio.usuario_repositorio import UsuarioRepositorio
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
        # Verificamos con una regex que el correo sea válido
        # En caso de que no sea válido, lanzamos una excepción
        if re.match(r"[^@]+@[^@]+\.[^@]+", correo_electronico) is None:
            raise ValueError("El correo electrónico no es válido")
        else:
            UsuarioRepositorio.crear_usuario(correo_electronico)

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
        time.sleep(10) #Simula que el usuario está viendo la peli/serie durante 10 segundos
        #funcion de la instancia de Media que hayamos recibido,
        #actualiza la lista de películas o series en el objeto y actualiza el usuario
        if isinstance(media, Pelicula):
            usuario.peliculas_vistas.append(media)

        elif isinstance(media, Serie):
            usuario.series_vistas.append(media)

        UsuarioRepositorio.actualiza_usuario(usuario)
