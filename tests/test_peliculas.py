"""Tests del catálogo: listado, detalle y géneros."""


def test_salud_responde_ok(cliente):
    respuesta = cliente.get("/salud")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"estado": "ok"}


def test_listar_devuelve_el_catalogo_completo(cliente):
    respuesta = cliente.get("/peliculas")
    assert respuesta.status_code == 200
    peliculas = respuesta.json()
    assert len(peliculas) == 50


def test_cada_pelicula_tiene_los_campos_esperados(cliente):
    primera = cliente.get("/peliculas").json()[0]
    for campo in ("id", "titulo", "anyo", "generos", "director", "duracion_min"):
        assert campo in primera, f"falta el campo {campo}"


def test_obtener_pelicula_existente(cliente):
    respuesta = cliente.get("/peliculas/1")
    assert respuesta.status_code == 200
    assert respuesta.json()["titulo"] == "Blade Runner"


def test_obtener_pelicula_inexistente_devuelve_404(cliente):
    respuesta = cliente.get("/peliculas/9999")
    assert respuesta.status_code == 404
    assert respuesta.json()["detail"] == "Película no encontrada"


def test_generos_sin_repeticiones_y_ordenados(cliente):
    generos = cliente.get("/generos").json()
    assert generos == sorted(generos)
    assert len(generos) == len(set(generos))
    assert "Ciencia ficción" in generos
