"""Ruta de estadísticas del catálogo."""

from fastapi import APIRouter

from app.models.peliculas import Estadisticas
from app.services import estadisticas as servicio

router = APIRouter(tags=["estadisticas"])


@router.get("/estadisticas", response_model=Estadisticas)
def obtener_estadisticas() -> dict:
    """Resumen agregado: totales, medias y reparto por década."""
    return servicio.calcular()
