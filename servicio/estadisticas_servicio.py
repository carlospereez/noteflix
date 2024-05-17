from modelo import Usuario
from typing import Tuple, Dict, List # Hacemos import de las más comunes porque luego las necesitaremos
class EstadisticasServicio:
    def obtener_estadisticas(self, usuario: Usuario):
        '''Por ahora esta función devuelve dos diccionarios pero creo que hace falta algo más'''
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

        return generos_peliculas, generos_series