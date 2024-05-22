from modelo import Usuario, Media, Pelicula, Serie
from typing import List
import time
import re
from modelo.repositorio.usuario_repositorio import UsuarioRepositorio

class UsuarioServicio:
    """
       Clase que representa el servicio de usuarios.

       Con esta clase podremos gestionar los usuarios haciendo uso del repositorio. Incluye la posibilidad de crear nuevos usuarios,
       la obtención de un usuario por su correo electrónico, la obtención de todos los usuarios y la
       visualización de contenido multimedia por parte de un usuario.

       Methods:
       alta_usuario(correo_electronico: str) -> None: Coge el mail y crea un usuario
       obtener_usuario(correo_electronico: str) -> Usuario: Devuelve un usuario por su correo electrónico.
       obtener_usuarios() -> List[Usuario]: Devuelve una lista de todos los usuarios.
       visualizar_media(usuario: Usuario, media: Media) -> None: Simulación de la visualización de una película o serie por parte de un usuario.
       """
    @classmethod
    def alta_usuario(cls, correo_electronico: str) -> None:
        """
        Crea un nuevo usuario con el correo electrónico dado.

        Esta función valida el correo electrónico introducido utilizando una expresión regular.
        Si el correo electrónico es válido, se crea un nuevo usuario.
        Si este no es válido, se lanza una excepción.
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
        Esta función simula la visualización de una película o serie de un usuario.
        Si se trata de una película, se añade a la lista de películas vistas del usuario y
        si se trata de una serie, se añade a la lista de series.
        Por último, se actualiza el usuario usando UsuarioRepositorio.actualiza_usuario(usuario)
        """
        time.sleep(10) #Simula que el usuario está viendo la peli/serie durante 10 segundos
        #funcion de la instancia de Media que hayamos recibido,
        #actualiza la lista de películas o series en el objeto y actualiza el usuario
        if isinstance(media, Pelicula):
            usuario.peliculas_vistas.append(media)

        elif isinstance(media, Serie):
            usuario.series_vistas.append(media)

        UsuarioRepositorio.actualiza_usuario(usuario)
