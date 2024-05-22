from typing import List, Tuple, Dict
from modelo import Usuario, Media, Pelicula, Serie
from servicio import EstadisticasServicio, MediaServicio
import pandas as pd
class RecomendacionesServicio:
    @classmethod
    def obtener_recomendaciones(cls, usuario: Usuario) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Genera recomendaciones de películas y series para un usuario basándose en sus géneros más vistos.

        Este método primero obtiene las estadísticas del usuario, ordena los géneros en orden descendente por recuento,
        y luego busca películas y series que pertenezcan a esos géneros hasta que tiene 3 de cada uno.
        El método devuelve las películas y series recomendadas.

        Parameters:
        usuario (Usuario): El usuario para quien generar las recomendaciones.

        Returns:
        Tuple[List[Pelicula], List[Serie]]: Una tupla que contiene dos listas. La primera lista contiene las películas
        recomendadas, y la segunda lista contiene las series recomendadas.
        """

        # Obtención de las estadísticas de películas y series vistas por el usuario
        estadisticas_peliculas_df, estadisticas_series_df, estadisticas_peliculas, estadisticas_series = (
            EstadisticasServicio.obtener_estadisticas_usuarios(usuario))  # Lo ponemos aquí porque no cabe

        # Unión de los diccionarios de estadísticas de películas y series en uno solo
        estadisticas_comunes: Dict[str, int] = estadisticas_peliculas.copy()  # Copiar estadísticas de películas

        for estadistica in estadisticas_series:
            # Si el género no está presente se añade al diccionario, si ya está presente se suma el valor
            if estadistica not in estadisticas_comunes:
                estadisticas_comunes[estadistica] = estadisticas_series[estadistica]
            else:
                estadisticas_comunes[estadistica] += estadisticas_series[estadistica]

        # Ordenado de géneros en orden descendente por recuento
        estadisticas_ordenadas: List[Tuple[str, int]] = sorted(estadisticas_comunes.items(), key=lambda x: x[1],
                                                               reverse=True)
        # Obtención de los 3 géneros más vistos
        generos_favoritos: List[str] = [genero[0] for genero in estadisticas_ordenadas[:3]]

        # Obtención de todas las películas y series disponibles
        peliculas: List[Pelicula] = MediaServicio.obtener_listado_peliculas()
        series: List[Serie] = MediaServicio.obtener_listado_series()

        # Diccionarios para almacenar las películas y series recomendadas junto con su peso
        peliculas_con_peso: Dict[Pelicula, int] = {}
        series_con_peso: Dict[Serie, int] = {}

        # Bucle para iterar sobre las películas y asignarles un peso en función de la cantidad de géneros coincidentes
        # con los favoritos
        for pelicula in peliculas:
            peso: int = 1  # Inicializar el peso de la película
            # Bucle para iterar sobre los géneros favoritos del usuario
            for genero in generos_favoritos:
                # Se incrementa el peso si el género está presente en los géneros de la película
                if genero in pelicula.generos:
                    peso += 1
            # Se asigna la película con su peso al diccionario películas_con_peso
            peliculas_con_peso[pelicula] = peso

        # Bucle para iterar sobre las series y asignarles un peso en función de la cantidad de
        # géneros coincidentes con los favoritos
        for serie in series:
            peso: int = 1  # Inicializar el peso de la serie
            # Bucle para iterar sobre los géneros favoritos del usuario
            for genero in generos_favoritos:
                # Se incrementa el peso si el género está presente en los géneros de la serie
                if genero in serie.generos:
                    peso += 1
            # Se asigna la serie con su peso al diccionario series_con_peso
            series_con_peso[serie] = peso

        # Se ordenan las películas y series recomendadas por peso y se toman las 5 primeras
        peliculas_escogidas: List[Pelicula] = [pelicula[0] for pelicula in
                                               sorted(peliculas_con_peso.items(), key=lambda x: x[1], reverse=True)[:5]]
        series_escogidas: List[Serie] = [serie[0] for serie in
                                         sorted(series_con_peso.items(), key=lambda x: x[1], reverse=True)[:5]]

        # Lista de listas para almacenar la información de las películas recomendadas
        peliculas_recomendadas_lista: List[List[str]] = []

        # Bucle para iterar sobre las películas escogidas y agregar la información requerida a la lista de listas
        for pelicula in peliculas_escogidas:
            str_peliculas_recomendadas: str = ""  # Reiniciar la cadena de géneros
            for genero in pelicula.generos:
                str_peliculas_recomendadas += f'{genero}, '  # Concatenar los géneros de la película a la cadena
            # Se verifica si la película está vista por el usuario y se asigna 'SÍ' o 'NO' a la variable vista
            if pelicula.id in [vst.id for vst in usuario.peliculas_vistas]:
                vista: str = 'SÍ'
            else:
                vista: str = 'NO'

            # Creación de una lista con la información de la película y agregación a la lista de películas recomendadas
            pelicula_info: List[str] = [
                pelicula.id,
                pelicula.titulo,
                pelicula.director,
                pelicula.anio,
                str_peliculas_recomendadas.strip(', '),  # Eliminar la última coma y el espacio
                pelicula.duracion,
                vista
            ]
            peliculas_recomendadas_lista.append(pelicula_info)

        # Se inicializa una lista vacía para almacenar la información de las series recomendadas
        series_recomendadas_lista: List[List[str]] = []

        # Bucle para iterar sobre las series escogidas y agregar la información requerida a la lista de listas
        for serie in series_escogidas:
            str_series_recomendadas: str = ""  # Reiniciar la cadena de géneros
            for genero in serie.generos:
                str_series_recomendadas += f'{genero}, '  # Concatenar los géneros de la serie a la cadena
            # Se verifica si la serie está vista por el usuario y se asigna 'SÍ' o 'NO' a la variable vista
            if serie.id in [vst.id for vst in usuario.series_vistas]:
                vista: str = 'SÍ'
            else:
                vista: str = 'NO'
            # Se crea una lista con la información de la serie y se agrega a la lista de series recomendadas
            serie_info: List[str] = [
                serie.id,
                serie.titulo,
                serie.director,
                serie.anio,
                str_series_recomendadas.strip(', '),  # Eliminar la última coma y el espacio
                serie.temporadas,
                vista
            ]
            series_recomendadas_lista.append(serie_info)

        # Conversión de las listas de películas y series recomendadas en DataFrames
        peliculas_recomendadas: pd.DataFrame = pd.DataFrame(peliculas_recomendadas_lista,
                                                            columns=['ID', 'Título', 'Director', 'Año', 'Géneros',
                                                                     'Duración',
                                                                     'Vista'])
        series_recomendadas: pd.DataFrame = pd.DataFrame(series_recomendadas_lista,
                                                         columns=['ID', 'Título', 'Director', 'Año', 'Géneros',
                                                                  'Temporadas',
                                                                  'Vista'])

        # Funciones de ajuste de DataFrames de pandas

        # Establecer el ancho máximo de las columnas para evitar el truncado de los datos
        pd.set_option('display.max_colwidth', None)

        # Evitar que los DataFrames se rompan en varias líneas
        pd.set_option('expand_frame_repr', False)

        # Mostrar todas las columnas
        pd.set_option('display.max_columns', None)

        # Mostrar todas las filas
        pd.set_option('display.max_rows', None)

        return peliculas_recomendadas, series_recomendadas