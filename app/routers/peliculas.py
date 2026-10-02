"""Rutas del catálogo de películas.

Regla del proyecto: aquí NO hay lógica de negocio. El router valida la entrada,
llama al servicio y traduce el resultado a HTTP.
"""

from fastapi import APIRouter, HTTPException, Query

from app.models.peliculas import Pelicula
from app.services import peliculas as servicio

router = APIRouter(tags=["peliculas"])


@router.get("/peliculas", response_model=list[Pelicula])
def listar_peliculas() -> list[dict]:
    """Devuelve el catálogo completo."""
    return servicio.listar()


@router.get("/generos", response_model=list[str])
def listar_generos() -> list[str]:
    """Devuelve los géneros presentes en el catálogo, ordenados."""
    return servicio.generos_disponibles()


@router.get("/buscar", response_model=list[Pelicula])
def buscar_peliculas(
    q: str = Query(min_length=1, description="Texto a buscar en el título."),
) -> list[dict]:
    """Busca por título, ignorando mayúsculas y tildes."""
    return servicio.buscar(q)


@router.get("/peliculas/{pelicula_id}", response_model=Pelicula)
def obtener_pelicula(pelicula_id: int) -> dict:
    """Devuelve una película por su id. 404 si no existe."""
    pelicula = servicio.obtener(pelicula_id)
    if pelicula is None:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return pelicula
