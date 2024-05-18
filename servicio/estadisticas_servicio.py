from modelo import Usuario
from typing import Tuple, Dict, List  # Hacemos import de las más comunes porque luego las necesitaremos
import pandas as pd
import matplotlib.pyplot as plt
class EstadisticasServicio:
    @classmethod
    def obtener_estadisticas(cls, usuario: Usuario)-> Tuple[pd.DataFrame, pd.DataFrame, Dict[str, int], Dict[str, int]]:
        """
        Obtiene las estadísticas de los géneros de las películas y series vistas por un usuario.

        Este método recorre las películas y series vistas por el usuario, y para cada género en cada película o
        serie, incrementa su recuento en los diccionarios correspondientes. Si un género no está presente
        en el diccionario, se añade con un recuento inicial de 1.

        Parametros:
        usuario (Usuario): El usuario para quien obtener las estadísticas.

        Returns:
        Tuple[pd.DataFrame, pd.DataFrame, Dict[str, int], Dict[str, int]]: Una tupla que contiene dos DataFrames y
        dos diccionarios. El primer diccionario contiene los recuentos de los géneros de las películas vistas por el
        usuario, y el segundo diccionario contiene los recuentos de los géneros de las series vistas por el usuario.
        Los DataFrames contienen lo mismo, la única diferencia es que son DataFrames y no diccionarios, pero son
        para que la información se muestre más ordenada y con mejor aspecto. Los diccionarios son utiles para
        otras funciones como obtener_grafico_estadisticas(usuario).
        """
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
    @classmethod
    def obtener_grafico_estadisticas(cls, usuario: Usuario):
        """
        Genera gráficos por sectores para visualizar las estadísticas de géneros de películas y series vistas por un
        usuario. Para poder representar los datos en los gráficos, primero hace falta separarlos en dos listas, que
        serán cuatro en realidad porque hay dos para películas y dos para series.

        Parameters:
        usuario (Usuario): El usuario para quien generar los gráficos.

        Returns:
        None
        """
        # Obtiene las estadísticas de géneros de películas y series
        generos_peliculas_df, generos_series_df, generos_peliculas, generos_series = cls.obtener_estadisticas(usuario)

        # Listas de claves y valores de géneros de películas
        claves_peliculas: List[str] = list(generos_peliculas.keys())
        valores_peliculas: List[int] = list(generos_peliculas.values())

        # Listas de claves y valores de géneros de series
        claves_series: List[str] = list(generos_series.keys())
        valores_series: List[int] = list(generos_series.values())

        # Gráfico de sectores para visualizar las estadísticas de géneros de películas
        plt.figure(figsize=(10, 6))  # Definición del tamaño del gráfico
        plt.pie(valores_peliculas, labels=claves_peliculas, autopct='%1.1f%%', startangle=140,
                colors=plt.cm.tab20.colors)  # Crea el gráfico
        plt.title('Visualizaciones por género - Películas')  # Título del gráfico
        plt.axis('equal')  # Asegura que el gráfico de sectores sea un círculo
        plt.tight_layout()  # Ajuste del diseño del gráfico para evitar superposiciones
        plt.show()  # Muestra el gráfico

        # Gráfico de sectores para visualizar las estadísticas de géneros de series
        plt.figure(figsize=(10, 6))  # Definición del tamaño del gráfico
        plt.pie(valores_series, labels=claves_series, autopct='%1.1f%%',startangle=140,
                colors=plt.cm.tab20.colors)  # Crea el gráfico
        plt.title('Visualizaciones por género - Series')  # Título del gráfico
        plt.axis('equal')  # Asegura que el gráfico de sectores sea un círculo
        plt.tight_layout()  # Ajuste del diseño del gráfico para evitar superposiciones
        plt.show()  # Muestra el gráfico

        return None