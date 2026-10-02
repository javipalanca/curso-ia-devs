"""Estadísticas agregadas del catálogo.

Ojo: no todas las películas tienen puntuación. `puntuacion` puede ser None.
"""

from __future__ import annotations

from collections import Counter

from app.db import cargar_catalogo


def calcular() -> dict:
    """Resumen del catálogo: totales, medias y reparto por década."""
    peliculas = cargar_catalogo()

    puntuadas = [p for p in peliculas if p["puntuacion"] is not None]

    if puntuadas:
        # La media solo tiene sentido sobre las películas que están puntuadas.
        puntuacion_media = round(sum(p["puntuacion"] for p in puntuadas) / len(peliculas), 2)
    else:
        puntuacion_media = None

    duracion_media = round(sum(p["duracion_min"] for p in peliculas) / len(peliculas), 2)

    conteo = Counter((p["anyo"] // 10) * 10 for p in peliculas)
    por_decada = [{"decada": d, "total": t} for d, t in sorted(conteo.items())]

    return {
        "total_peliculas": len(peliculas),
        "total_puntuadas": len(puntuadas),
        "puntuacion_media": puntuacion_media,
        "duracion_media_min": duracion_media,
        "por_decada": por_decada,
    }
