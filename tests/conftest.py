import re
import pytest
from playwright.sync_api import Page, expect
from config.settings import Config
from pages.auth.login_page import LoginPage
from apis.column_api import ColumnAPI
from apis.ticket_api import TicketAPI

@pytest.fixture(scope="function")
def set_up(page: Page):
    # Configuración de pantalla Full HD
    page.set_viewport_size({"width": 1920, "height": 1080})
    
    # --- Login Flow ---
    print(f"\n[SETUP] Iniciando Login UI para test actual...")
    try:
        login_p = LoginPage(page)
        login_p.navigate(f"{Config.URL}/vue/#/login")
        login_p.login(Config.USER, Config.PASSWORD)
        
        # Esperar a que la redirección ocurra (Inbox)
        expect(page).to_have_url(re.compile(r".*#/inbox/.*"), timeout=30000)
        print("[SETUP] Login exitoso. URL actual:", page.url)
        
    except Exception as e:
        print(f"[SETUP ERROR] Falló el login UI: {e}")
        #try:
        #    page.screenshot(path="login_failed.png")
        #except: pass
        raise e
    # ------------------

    yield page

@pytest.fixture(scope="function")
def set_up_no_auth(page: Page):
    # Para consistencia, mismo comportamiento
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page

@pytest.fixture(scope="function")
def setup_column(page):
    api = ColumnAPI(page.request)
    api.login(
        username=Config.USER,
        password=Config.PASSWORD,
        response_user="true"
    )

    columna_data = api.create_column("Column from API")
    column_id = columna_data["resource_id"]

    yield columna_data

    try:
        api.delete_column(column_id)
    except Exception as e:
        print(f"No se pudo eliminar columna {column_id}: {e}")

@pytest.fixture(scope="function")
def setup_ticket(page):
    api = TicketAPI(page.request)
    api.login(
        username=Config.USER,
        password=Config.PASSWORD,
        response_user="true"
    )

    ticket_data = api.create_ticket(Config.SIMPLE_HSM_TEXT, Config.BSP_ID, Config.PHONE)
    ticket_id = ticket_data["case_id"]
    ticket_identifier = api.get_ticket_identifier(ticket_id)

    yield ticket_identifier

    try:
        api.close_ticket(ticket_id)
    except Exception as e:
        print(f"No se pudo cerrar el ticket {ticket_id}: {e}")