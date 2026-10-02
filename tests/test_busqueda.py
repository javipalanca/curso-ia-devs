"""Tests de la búsqueda por título."""


def test_busqueda_encuentra_por_texto_exacto(cliente):
    resultados = cliente.get("/buscar", params={"q": "Matrix"}).json()
    assert [p["titulo"] for p in resultados] == ["The Matrix"]


def test_busqueda_ignora_mayusculas(cliente):
    resultados = cliente.get("/buscar", params={"q": "matrix"}).json()
    assert len(resultados) == 1


def test_busqueda_ignora_tildes(cliente):
    resultados = cliente.get("/buscar", params={"q": "parasitos"}).json()
    assert [p["titulo"] for p in resultados] == ["Parásitos"]


def test_busqueda_parcial_devuelve_varias(cliente):
    resultados = cliente.get("/buscar", params={"q": "dune"}).json()
    assert len(resultados) == 2


def test_busqueda_sin_resultados_devuelve_lista_vacia(cliente):
    resultados = cliente.get("/buscar", params={"q": "zzzzz"}).json()
    assert resultados == []


def test_busqueda_vacia_es_error_de_validacion(cliente):
    assert cliente.get("/buscar", params={"q": ""}).status_code == 422
