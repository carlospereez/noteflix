from __future__ import annotations
from typing import List
from modelo import Pelicula
from modelo.serie import Serie
import json

class MediaRepositorio:

    FICHERO_MEDIA = 'resources/catalogo.json'

    @classmethod
    def obtener_peliculas(cls) -> List[Pelicula]:
        with open(cls.FICHERO_MEDIA, 'r') as f:
            data = json.load(f)

        peliculas = []
        for p in data['films']:
            pelicula = Pelicula(p['id'], p['title'], p['director'], p['year'], p['tags'], p['duration'])
            peliculas.append(pelicula)

        return peliculas

    @classmethod
    def obtener_series(cls) -> List[Serie]:
        with open(cls.FICHERO_MEDIA, 'r') as f:
            data = json.load(f)

        series = []
        for s in data['series']:
            serie = Serie(s['id'], s['title'], s['director'], s['year'], s['tags'], s['seasons'])
            series.append(serie)

        return series

    @classmethod
    def obtener_pelicula_por_id(cls, id_pelicula: str) -> Pelicula | None:
        with open(cls.FICHERO_MEDIA, 'r') as f:
            data = json.load(f)

        for p in data['films']:
            if p['id'] == id_pelicula:
                return Pelicula(p['id'], p['title'], p['director'], p['year'], p['tags'], p['duration'])

        return None

    @classmethod
    def obtener_serie_por_id(cls, id_serie: str) -> Serie | None:
        with open(cls.FICHERO_MEDIA, 'r') as f:
            data = json.load(f)

        for s in data['series']:
            if s['id'] == id_serie:
                return Serie(s['id'], s['title'], s['director'], s['year'], s['tags'], s['seasons'])

        return None
