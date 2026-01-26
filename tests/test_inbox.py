from playwright.sync_api import expect
from pages.inbox.inbox_page import InboxPage
import pytest

@pytest.mark.skip
def test_create_column(set_up):
    page = set_up
    inbox_p = InboxPage(page)

    modal = inbox_p.sidebar.open_new_column_modal()
    modal.wait_until_visible()
    modal.fill_and_save("Ventas")

@pytest.mark.skip
def test_edit_exiting_column(set_up):
    page = set_up
    inbox_p = InboxPage(page)

    column_venta = inbox_p.get_column("Ventas")
    modal_edit = column_venta.select_edit_option()
    modal_edit.fill_and_save("Ventas update", is_edit=True)

    expect(inbox_p.get_column("Ventas update").title).to_be_visible()

def test_delete_column_successfully(set_up):
    page = set_up
    inbox = InboxPage(page)
    
    nombre_columna = "Ventas update"
    # 1. Obtenemos el componente de la columna
    columna = inbox.get_column(nombre_columna)
    
    # Guardamos el locator de la raíz antes de que se borre para poder verificarlo
    root_locator = columna.root 

    # 2. FLUJO ENCADENADO: Columna -> Modal -> Confirmar -> Regresa Inbox
    columna.select_delete_option().confirm_deletion()

    # 3. VERIFICACIÓN (Al no haber alerta, verificamos el DOM directamente)
    # expect(...).to_be_hidden() es la forma más limpia de confirmar la eliminación
    expect(root_locator).to_be_hidden(timeout=10000)