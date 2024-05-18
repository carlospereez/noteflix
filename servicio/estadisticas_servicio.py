from modelo import Usuario
from typing import Tuple, Dict, List  # Hacemos import de las más comunes porque luego las necesitaremos
import pandas as pd
class EstadisticasServicio:
    @classmethod
    def obtener_estadisticas(cls, usuario: Usuario)-> Tuple[pd.DataFrame, pd.DataFrame, Dict[str, int], Dict[str, int]]:
        # Diccionarios para almacenar los recuentos de géneros de películas y series
        generos_peliculas: Dict[str, int] = {}
        generos_series: Dict[str, int] = {}

        # Bucle para recorrer todas las películas vistas por el usuario
        for pelicula in usuario.peliculas_vistas:
            # Incrementa el recuento de géneros de películas
            for genero in pelicula.generos:
                if genero not in generos_peliculas:
                    generos_peliculas[genero] = 1
                else:
                    generos_peliculas[genero] += 1

        # Bucle para recorrer todas las series vistas por el usuario
        for serie in usuario.series_vistas:
            # Incrementa el recuento de géneros de series
            for genero in serie.generos:
                if genero not in generos_series:
                    generos_series[genero] = 1
                else:
                    generos_series[genero] += 1

        # Diccionarios para almacenar los géneros y visualizaciones de películas y series
        # para crear un DataFrame a partir de un diccionario con listas como valores
        generos_peliculas_dict: Dict[str, list] = {}
        generos_series_dict: Dict[str, list] = {}

        # Pares clave-valor de los diccionarios
        generos_peliculas_dict['Género'] = []
        generos_peliculas_dict['Visualizaciones'] = []
        generos_series_dict['Género'] = []
        generos_series_dict['Visualizaciones'] = []

        # Bucles para completar los diccionarios con los datos obtenidos
        for genero, visualizaciones in generos_peliculas.items():
            generos_peliculas_dict['Género'].append(genero)
            generos_peliculas_dict['Visualizaciones'].append(visualizaciones)

        for genero, visualizaciones in generos_series.items():
            generos_series_dict['Género'].append(genero)
            generos_series_dict['Visualizaciones'].append(visualizaciones)

        # Creación de DataFrames a partir de los diccionarios anteriores
        generos_peliculas_df: pd.DataFrame = pd.DataFrame(generos_peliculas_dict)
        generos_series_df: pd.DataFrame = pd.DataFrame(generos_series_dict)

        # Devuelve los DataFrames y los diccionarios
        return generos_peliculas_df, generos_series_df, generos_peliculas, generos_series
