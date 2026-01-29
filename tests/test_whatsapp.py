from apis.tester_api import TesterAPI
from config.settings import Config
from pages.inbox.case_view_page import CaseViewPage
from playwright.sync_api import expect
import pytest

@pytest.mark.skip
def test_whatsapp_message_persistence(set_up):
    MSG_TESTER = "Mensaje de prueba desde el tester"
    MSG_EXECUTIVE = "Hola buenas tardes desde Adereso Desk"
    # Arrange
    # - Enviar el mensaje incial del cliente via Tester API.
    page = set_up
    api = TesterAPI(page.request)
    api.login(Config.USER, Config.PASSWORD)

    ticket_id = api.send_message_by_tester(
        Config.ACCOUNT_NUMBER, 
        MSG_TESTER,
        "tester"
    )    
    # - Obtener el identificador del ticket a partir del id via API.
    identifier = api.get_identifier_from_ticket_id(ticket_id)

    # Act
    # - Navegar al ticket.
    case_view = CaseViewPage(page)
    case_view.go_to_ticket(identifier)
    expect(case_view.chat.last_message).to_contain_text(MSG_TESTER)
    # - Escribir una respuesta en el footer.
    # - Clic en enviar.
    case_view.footer.send_message_reply(MSG_EXECUTIVE)

    # Assert
    # - Validar que el mensaje enviado desde la aplicación aparezca en el chat con check enviado.
    expect(case_view.chat.last_message).to_contain_text(MSG_EXECUTIVE)
    # - Validar que el identificador es el correcto en el header.
    expect(case_view.header.id_label).to_contain_text(f"{identifier}")
    # - Validar que el estado del ticket es abierto.
    expect(case_view.footer.status_text_label).to_contain_text("Abierto")
    # Postcondiciones:
    # - Cerrar el ticket creado.
    api.close_ticket(ticket_id)

def test_send_image_whatsapp(setup_ticket, set_up):
    MSG_EXECUTIVE = "Hola buenas tardes de parte de Rick Sanchez"
    # Arrange
    # - Crear un ticket inicial.
    # - Obtener el id del ticket.
    ticket_id = setup_ticket
    # Act
    # - Navegar al ticket.
    page = set_up
    case_view = CaseViewPage(page)
    case_view.go_to_ticket(ticket_id)
    # - Seleccionar una imagen como adjunto al mensaje.
    image_path = "tests/resources/morty.jpg"
    # - Escribir una respuesta en el footer.
    # - Clic en enviar.
    alert = case_view.footer.attach_and_send(MSG_EXECUTIVE, image_path)
    # - Esperar alerta de envio
    # Esperar hasta 60 segundos (ambiente de pruebas es lento)
    alert.wait_for_success_send(60000)
    expect(case_view.chat.last_message).to_contain_text(MSG_EXECUTIVE, timeout=10000)
    # Asert
    # - Validar que el mensaje enviado desde la aplicación aparezca en el chat junto a la imagen renderizada.
    src = case_view.chat.get_src_image_message()
    assert src.startswith("http"), f"El src no es una URL válida: {src}"
    # - Validar el check de enviado del mensaje.
    expect(case_view.chat.first_check).to_be_visible()
    # - Validar que el estado del ticket es abierto.
    expect(case_view.footer.status_text_label).to_contain_text("Abierto")
    # Postcondiciones:
    # - Cerrar el ticket creado.