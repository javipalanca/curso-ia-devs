"""Esquemas de entrada y salida de la API. Pydantic v2.

Regla del proyecto: en esta capa NO hay lógica de negocio ni nada de HTTP.
Solo la forma de los datos.
"""

from pydantic import BaseModel, Field


class Pelicula(BaseModel):
    """Una película tal y como la devuelve la API."""

    id: int = Field(description="Identificador único, estable entre arranques.")
    titulo: str
    anyo: int = Field(description="Año de estreno.")
    generos: list[str] = Field(default_factory=list)
    director: str
    duracion_min: int
    puntuacion: float | None = Field(
        default=None,
        description="Nota media de 0 a 10. Puede ser None: no todas las películas están puntuadas.",
    )


class EstadisticasPorDecada(BaseModel):
    decada: int = Field(description="Década de estreno, por ejemplo 1990.")
    total: int


class Estadisticas(BaseModel):
    """Resumen del catálogo."""

    total_peliculas: int
    total_puntuadas: int
    puntuacion_media: float | None
    duracion_media_min: float
    por_decada: list[EstadisticasPorDecada]
