"""Fixtures compartidas por todos los tests."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def cliente() -> TestClient:
    """Cliente HTTP de pruebas contra la aplicación, sin levantar un servidor real."""
    return TestClient(app)
