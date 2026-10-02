"""Tests de las estadísticas del catálogo."""

from app.db import cargar_catalogo


def test_totales(cliente):
    datos = cliente.get("/estadisticas").json()
    assert datos["total_peliculas"] == 50
    assert datos["total_puntuadas"] == 47


def test_por_decada_suma_el_total(cliente):
    datos = cliente.get("/estadisticas").json()
    suma = sum(fila["total"] for fila in datos["por_decada"])
    assert suma == datos["total_peliculas"]


def test_duracion_media_es_razonable(cliente):
    datos = cliente.get("/estadisticas").json()
    assert 90 < datos["duracion_media_min"] < 160


def test_puntuacion_media_solo_cuenta_las_peliculas_puntuadas(cliente):
    """La media debe calcularse sobre las películas QUE TIENEN nota.

    Si se divide entre el total del catálogo, las tres películas sin puntuar
    arrastran la media hacia abajo y el número que publicamos es falso.
    """
    notas = [p["puntuacion"] for p in cargar_catalogo() if p["puntuacion"] is not None]
    esperada = round(sum(notas) / len(notas), 2)

    datos = cliente.get("/estadisticas").json()
    assert datos["puntuacion_media"] == esperada


def test_puntuacion_media_esta_en_el_rango_de_las_notas(cliente):
    """Una media nunca puede quedar por debajo de la nota más baja del conjunto."""
    notas = [p["puntuacion"] for p in cargar_catalogo() if p["puntuacion"] is not None]
    datos = cliente.get("/estadisticas").json()
    assert min(notas) <= datos["puntuacion_media"] <= max(notas)
