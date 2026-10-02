"""API de películas — proyecto del curso de desarrollo de software asistido por IA (UPV).

Arrancar en desarrollo:
    uv run uvicorn app.main:app --reload

Documentación interactiva: http://localhost:8000/docs
"""

from fastapi import FastAPI

from app.routers import estadisticas, peliculas

app = FastAPI(
    title="API de películas",
    description="Catálogo de películas del curso. Deliberadamente pequeño y sin base de datos.",
    version="0.1.0",
)

app.include_router(peliculas.router)
app.include_router(estadisticas.router)


@app.get("/salud", tags=["sistema"])
def salud() -> dict:
    """Comprobación de vida. Útil para verificar que el servidor arranca."""
    return {"estado": "ok"}
