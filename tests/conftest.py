import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def set_up(page: Page):
    # Configuración de pantalla Full HD
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    # Aquí iría lógica de cierre si fuera necesaria