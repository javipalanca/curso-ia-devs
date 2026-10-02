# API de películas

Proyecto que atraviesa las cinco sesiones del curso *Desarrollo de software asistido por IA* (UPV).
Es deliberadamente pequeño: catálogo en un JSON, sin base de datos, sin autenticación.
Lo importante no es el proyecto, es lo que le vamos haciendo encima.

## Arrancar

```bash
uv sync                                  # instala dependencias
uv run uvicorn app.main:app --reload     # servidor en http://localhost:8000
uv run pytest                            # tests
uv run ruff check .                      # linter
```

La documentación interactiva queda en <http://localhost:8000/docs>.

Sin `uv` (por ejemplo, en una máquina donde no puedes instalar nada):

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]" || pip install fastapi "uvicorn[standard]" pydantic httpx pytest ruff
python -m pytest
```

## Endpoints

| Método | Ruta | Qué hace |
|---|---|---|
| `GET` | `/salud` | Comprobación de vida |
| `GET` | `/peliculas` | Catálogo completo |
| `GET` | `/peliculas/{id}` | Una película. 404 si no existe |
| `GET` | `/buscar?q=` | Búsqueda por título, ignora mayúsculas y tildes |
| `GET` | `/generos` | Géneros presentes en el catálogo |
| `GET` | `/estadisticas` | Totales, medias y reparto por década |

## Estructura

```
app/
  main.py          arranque de FastAPI y registro de routers
  db.py            carga del catálogo desde datos/peliculas.json
  models/          esquemas Pydantic de entrada y salida
  routers/         rutas HTTP. Sin lógica de negocio
  services/        lógica de negocio. Sin nada de HTTP
datos/
  peliculas.json   el catálogo: 50 películas
tests/             tests con pytest y TestClient
```

La separación `routers` / `services` es la convención central del proyecto: un servicio
tiene que poder probarse sin levantar el servidor, y un router no debe contener decisiones.

## Estado actual

Hay **un test que falla**. Es intencionado: forma parte de la práctica de depuración de la
sesión 2. No lo arregles antes de tiempo.

```bash
uv run pytest -q
```

## Datos

`datos/peliculas.json` contiene 50 películas con `id`, `titulo`, `anyo`, `generos`,
`director`, `duracion_min` y `puntuacion`.

**`puntuacion` puede ser `null`.** No todas las películas del catálogo están puntuadas.
Cualquier cálculo que las agregue tiene que tenerlo en cuenta.
