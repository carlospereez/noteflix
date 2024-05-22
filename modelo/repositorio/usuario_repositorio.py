from typing import List, Dict, Tuple
from modelo import Usuario, Pelicula, Serie
from excepciones import UsuarioYaRegistradoError
import pickle
from .media_repositorio import MediaRepositorio
class UsuarioRepositorio:

    FICHERO_USUARIOS = 'resources/usuarios.pickle'

    @classmethod
    def crear_usuario(cls, correo_electronico: str) -> None:
        try:
            with open(cls.FICHERO_USUARIOS, 'rb') as f:
                usuarios_fichero: Dict[str, List[List[str]]] = pickle.load(f)
        except FileNotFoundError:
            usuarios_fichero = {}

        if correo_electronico not in usuarios_fichero:
            usuarios_fichero[correo_electronico] = [[], []]

            with open(cls.FICHERO_USUARIOS, 'wb') as f:
                pickle.dump(usuarios_fichero, f)

        else:
            raise UsuarioYaRegistradoError()

    @classmethod
    def obtener_usuario(cls, correo_electronico: str) -> Usuario | None:
        try:
            with open(cls.FICHERO_USUARIOS, 'rb') as f:
                usuarios_fichero: Dict[str, List[List[str]]] = pickle.load(f)
        except FileNotFoundError:
            return None

        if correo_electronico in usuarios_fichero:
            lista_peliculas, lista_series = cls._obtener_peliculas_y_series_vistas(usuarios_fichero[correo_electronico])

            return Usuario(correo_electronico, lista_peliculas, lista_series)

        return None

    @classmethod
    def obtener_usuarios(cls) -> List[Usuario]:

        usuarios = []

        try:
            with open(cls.FICHERO_USUARIOS, 'rb') as f:
                usuarios_fichero: Dict[str, List[List[str]]] = pickle.load(f)
        except FileNotFoundError:
            return usuarios

        for usuario in usuarios_fichero:
            lista_peliculas, lista_series = cls._obtener_peliculas_y_series_vistas(usuarios_fichero[usuario])
            usuarios.append(Usuario(usuario, lista_peliculas, lista_series))

        return usuarios

    @classmethod
    def actualiza_usuario(cls, usuario: Usuario) -> None:

        try:
            with open(cls.FICHERO_USUARIOS, 'rb') as f:
                usuarios = pickle.load(f)
        except FileNotFoundError:
            usuarios = {}

        ids_peliculas_vistas = [p.id for p in usuario.peliculas_vistas]
        ids_series_vistas = [s.id for s in usuario.series_vistas]

        usuarios[usuario.correo_electronico] = [ids_peliculas_vistas, ids_series_vistas]

        with open(cls.FICHERO_USUARIOS, 'wb') as f:
            pickle.dump(usuarios, f)

    @classmethod
    def _obtener_peliculas_y_series_vistas(cls, ids_media_visto: List[List[str]]) -> Tuple[List[Pelicula], List[Serie]]:
        lista_peliculas: List[Pelicula] = []
        lista_series: List[Serie] = []

        for id_pelicula in ids_media_visto[0]:
            pelicula = MediaRepositorio.obtener_pelicula_por_id(id_pelicula)
            if pelicula is not None:
                lista_peliculas.append(pelicula)

        for id_serie in ids_media_visto[1]:
            serie = MediaRepositorio.obtener_serie_por_id(id_serie)
            if serie is not None:
                lista_series.append(serie)

        return lista_peliculas, lista_series
