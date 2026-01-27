import pytest
from pages.inbox.inbox_page import InboxPage
from playwright.sync_api import expect

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

def test_creation_of_proactive_ticket_with_cross_validation(setup_column, set_up):
    page = set_up
    column_id, column_name = setup_column["resource_id"], setup_column["name"]
    print(f"La columna {column_name} corresponde al id: {column_id}")

@pytest.mark.skip
def test_validate_open_status_ticket(set_up):
    page = set_up
    inbox = InboxPage(page)
    columna = inbox.get_column("Ventas update")

    ticket_id = "9256"
    ticket = columna.get_ticket_by_id(ticket_id)

    expect(ticket.get_ticket_status()).to_have_text("Abierto", timeout=10000)