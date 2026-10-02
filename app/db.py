"""Carga del catálogo desde datos/peliculas.json.

El catálogo se lee una sola vez al importar el módulo y se guarda en memoria.
Es un curso, no un sistema en producción: no hay base de datos real ni ORM.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FICHERO_DATOS = RAIZ / "datos" / "peliculas.json"


@lru_cache(maxsize=1)
def cargar_catalogo() -> list[dict]:
    """Devuelve la lista completa de películas como diccionarios.

    Cacheado: se lee del disco una única vez por proceso.
    """
    with FICHERO_DATOS.open(encoding="utf-8") as f:
        return json.load(f)
