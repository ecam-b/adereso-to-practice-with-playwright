from pages.inbox.inbox_page import InboxPage
from playwright.sync_api import expect
from config.settings import Config

def test_create_information_campaign(set_up, unique_name):
    
    # Arrange
    # - Ingresar a la aplicación con credenciales de Administrador.
    # - Data Prep: Contar con una Plantilla HSM previamente aprobada por Meta.
    # Act
    # - Navegar al módulo de Campañas.
    page = set_up
    inbox = InboxPage(page)
    campaigns_page = inbox.topmenu.go_to_engage()
    #expect(campaign.btn_create_campaign).to_be_visible(timeout=10000)
    # - Clic en "Crear campaña".
    new_campaign_p = campaigns_page.click_create_campaign()
    # - Completar el formulario:
    #     - Nombre: Asignar un nombre único (ej. Campaña_Automation_[Timestamp]).
    #     - Cuenta: Seleccionar la cuenta de WhatsApp autorizada.
    #     - Plantilla HSM: Seleccionar la plantilla.
    # - Carga de Archivo: Subir el archivo de destinatarios.
    # - Marcar el check de confirmación de envío y clic en "Crear campaña".
    ## test data
    NAME = unique_name
    ACCOUNT = Config.ACCOUNT_NAME
    HSM = Config.SIMPLE_HSM_TEXT
    recipients_path = {
        "path": "tests/resources/numero_solamente.csv",
        "name": "numero_solamente.csv"
    }
    campaigns_page = new_campaign_p.create_simple_campaign(NAME, ACCOUNT, HSM, recipients_path)
    # campaigns_page.alert.wait_for_toast("Campaña creada exitosamente", timeout=5000)
    # - Clic en "Enviar campaña" de la recien creada.
    campaign = campaigns_page.get_campaign_row(NAME)
    expect(campaign.get_status()).to_contain_text("Cargada")
    campaign.send()
    
    campaigns_page.alert.wait_for_toast("Enviando campaña")
    # Assert
    # - Validar que el estado de la fila correspondiente cambie a "Enviando...".
    expect(campaign.get_status()).to_contain_text("Enviando...")
    # - Acción Intermedia: Crear una columna dinámica (vía API o UI) filtrada por el ID o Nombre de la campaña recién enviada.
    # - Validar que el mensaje en el chat coincida con el texto de la Plantilla HSM.
    # - Validar que el estado del ticket es "Cerrado".
    # Postcondiciones:
    # - Eliminar la columna creada para la validación.