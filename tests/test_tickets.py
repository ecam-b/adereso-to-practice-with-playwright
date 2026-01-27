import pytest
from pages.inbox.inbox_page import InboxPage
from playwright.sync_api import expect
from config.settings import Config

@pytest.mark.skip
def test_creation_of_proactive_ticket_with_cross_validation(setup_column, set_up):
    # contantes del test
    ACCOUNT = "Adereso BSP One (56949591142)"
    DEPARTMENT = "Sin departamento"
    TEMPLATE = Config.SIMPLE_HSM_TEXT
    PHONE = "+573115734967"
    # 1. Realizar el login
    # 2. Esperar a que el inbox cargue correctamente
    page = set_up
    inbox = InboxPage(page)
    # 3. Click en el boton "Crear nuevo ticket"
    # 4. Esperar a que el modal cargue
    modal = inbox.sidebar.open_new_ticket_modal()
    # 5. Seleccionar la cuenta de origen "Adereso BSP One (56949591142)"
    # 6. Seleccionar un departamento "Sin departamento"
    # 7. Seleccionar una plantilla "qa_test_simple_text_1"
    # 8. Llenar el campo Cliente con el numero de telefono "+573115734967"
    # 9. Click en "Enviar mensaje"
    alert = modal.creat_new_ticket(
        ACCOUNT,
        DEPARTMENT,
        TEMPLATE,
        PHONE
    )
    # 10. Esperar a que desaparezca el modal
    expect(modal.container).to_be_hidden(timeout=30000)
    # 11. Validar que aparezca la alerta de creación exitosa con el link del ticket.
    alert.wait_until_visible()
    expect(alert.container).to_contain_text("HSM enviado exitosamente")
    # 12. Hacer clic en el enlace del ticket dentro de la alerta de éxito.
    case_view = alert.go_to_new_ticket() #uid
    # 13. Extraer el ID del ticket desde el encabezado del detalle.
    # .strip() quita espacios y saltos de linea
    ticket_id = case_view.get_id_label().inner_text().strip() # obtiene el text visible del locator mediante .inner_text() #id tipo: 9455
    print(f"El id del ticket creado es: {ticket_id}") 
    # 14. Volver al inbox y validar que el ticket aparezca en la columna disponibles mediante su id.
    column = case_view.get_column()
    column.refresh_if_needed(timeout=20000)
    ticket = column.get_ticket_by_id(ticket_id)

    expect(ticket.id_label).to_have_text(ticket_id)

def test_view_ticket_details(setup_ticket, set_up):
    # Precondiciones:
    # Tener un ticket creado previamente (idealmente vía API para asegurar consistencia de datos).
    pass
    # Pasos:
    # 1. Realizar el login: Acceder con credenciales válidas.
    # 2. Carga del Inbox: Esperar a que la interfaz principal y las columnas estén visibles.
    # 3. Acceso al Ticket: Localizar el ticket (ID 9266) en la columna correspondiente y hacer clic para abrir el CaseView.
    # 4. Validación de Identidad (Header):
    # - Verificar que el nombre del cliente sea Elian.
    # - Verificar que el ID en el encabezado coincida con 9266.
    # - Confirmar que aparezca el icono de WhatsApp como canal de origen.
    # - Validar que el número de contacto sea 573115734967.
    # 5. Validación de Contenido (Chat):
    # - Confirmar la presencia del mensaje: "Cordial saludo estimado usuario...".
    # - Verificar que el mensaje tenga la marca de tiempo y el doble check azul de entregado.
    # 6. Validación de Estado y Asignación (Bottom Bar):
    # - Asegurar que el selector de estado indique Abierto.
    # 7. Validación de Navegación Lateral (Right Sidebar):
    # - Verificar que los iconos de los menús laterales (Info, Cliente, Historial, etc.) sean visibles y clicables.

    # Postcondiciones:
    # Cerrar el ticket previamente creado (idealmente vía API para asegurar consistencia de datos).

@pytest.mark.skip
def test_interact_with_specific_ticket(set_up):
    page = set_up
    inbox = InboxPage(page)

    columna = inbox.get_column("Ventas update")
    print(f"Tickets físicos en columna: {columna.get_all_tickets_count()}")

    #buscar id especifico
    ticket_id = "9252"
    case_view = columna.get_ticket_by_id(ticket_id).open_detail()

    expect(case_view.get_id_label()).to_contain_text(ticket_id)


@pytest.mark.skip
def test_validate_open_status_ticket(set_up):
    page = set_up
    inbox = InboxPage(page)
    columna = inbox.get_column("Ventas update")

    ticket_id = "9256"
    ticket = columna.get_ticket_by_id(ticket_id)

    expect(ticket.get_ticket_status()).to_have_text("Abierto", timeout=10000)