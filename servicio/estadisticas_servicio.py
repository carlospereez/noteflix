from modelo import Usuario
from typing import Tuple, Dict, List  # Hacemos import de las más comunes porque luego las necesitaremos
import pandas as pd
import matplotlib.pyplot as plt
class EstadisticasServicio:
    @classmethod
    def obtener_estadisticas_usuario(cls, usuario: Usuario)-> Tuple[pd.DataFrame, pd.DataFrame, Dict[str, int], Dict[str, int]]:
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

    @classmethod
    def peliculas_series_vistas(cls, usuario: Usuario) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Genera DataFrames con las películas y series vistas por un usuario, evitando duplicados.

        Parameters:
        usuario (Usuario): El usuario para quien generar los DataFrames.

        Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Dos DataFrames, uno para películas vistas y otro para series vistas.
        """

        # Listas para almacenar información de películas y series vistas
        peliculas_vistas: List[List] = []
        series_vistas: List[List] = []

        # Bucle para iterar sobre las películas vistas por el usuario
        for pelicula in usuario.peliculas_vistas:
            # Si la película no está en la lista de películas vistas, la agrega
            if pelicula.id not in [vista[0] for vista in peliculas_vistas]:
                str_peliculas_vistas = ""  # Reiniciar la cadena de géneros
                for genero in pelicula.generos:
                    str_peliculas_vistas += f'{genero}, '
                pelicula_vista_info = [  # Añadimos en orden los atributos de cada película a la lista
                    pelicula.id,
                    pelicula.titulo,
                    pelicula.director,
                    pelicula.anio,
                    str_peliculas_vistas.strip(', '),  # Elimina la última coma y el espacio
                    pelicula.duracion
                ]
                peliculas_vistas.append(pelicula_vista_info)

        # Bucle para iterar sobre las series vistas por el usuario
        for serie in usuario.series_vistas:
            # Si la serie no está en la lista de series vistas, la agrega
            if serie.id not in [vista[0] for vista in series_vistas]:
                str_series_vistas = ""  # Reiniciar la cadena de géneros
                for genero in serie.generos:
                    str_series_vistas += f'{genero}, '
                serie_vista_info = [  # Añadimos en orden los atributos de cada serie a la lista
                    serie.id,
                    serie.titulo,
                    serie.director,
                    serie.anio,
                    str_series_vistas.strip(', '),  # Elimina la última coma y el espacio
                    serie.temporadas
                ]
                series_vistas.append(serie_vista_info)

        # Convierte las listas de películas y series vistas en DataFrames
        peliculas_vistas_df = pd.DataFrame(peliculas_vistas,
                                           columns=['ID', 'Título', 'Director', 'Año', 'Géneros', 'Duración'])
        series_vistas_df = pd.DataFrame(series_vistas,
                                        columns=['ID', 'Título', 'Director', 'Año', 'Géneros', 'Temporadas'])

        # Configuraciones de visualización de los DataFrames
        pd.set_option('display.max_colwidth', None)  # Ancho máximo de columnas
        pd.set_option('expand_frame_repr', False)  # Evitar que los DataFrames se rompan en varias líneas
        pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
        pd.set_option('display.max_rows', None)  # Mostrar todas las filas

        return peliculas_vistas_df, series_vistas_df