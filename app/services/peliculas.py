"""Lógica de negocio del catálogo.

Regla del proyecto: en esta capa NO se importa nada de FastAPI ni de HTTP.
Estas funciones se pueden probar sin levantar el servidor.
"""

from __future__ import annotations

import unicodedata

from app.db import cargar_catalogo


def _normalizar(texto: str) -> str:
    """Pasa a minúsculas y quita tildes, para que la búsqueda sea tolerante.

    'Parásitos' y 'parasitos' deben encontrar lo mismo.
    """
    sin_tildes = unicodedata.normalize("NFD", texto)
    sin_tildes = "".join(c for c in sin_tildes if unicodedata.category(c) != "Mn")
    return sin_tildes.lower().strip()


def listar() -> list[dict]:
    """Todas las películas del catálogo, en el orden del fichero."""
    return list(cargar_catalogo())


def obtener(pelicula_id: int) -> dict | None:
    """Una película por su id, o None si no existe."""
    for pelicula in cargar_catalogo():
        if pelicula["id"] == pelicula_id:
            return pelicula
    return None


def buscar(consulta: str) -> list[dict]:
    """Películas cuyo título contiene la consulta.

    Ignora mayúsculas y tildes. Una consulta vacía no devuelve nada:
    preferimos una lista vacía a devolver el catálogo entero por accidente.
    """
    aguja = _normalizar(consulta)
    if not aguja:
        return []
    return [p for p in cargar_catalogo() if aguja in _normalizar(p["titulo"])]


def generos_disponibles() -> list[str]:
    """Lista ordenada y sin repeticiones de los géneros del catálogo."""
    generos: set[str] = set()
    for pelicula in cargar_catalogo():
        generos.update(pelicula["generos"])
    return sorted(generos)
