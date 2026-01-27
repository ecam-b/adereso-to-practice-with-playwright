from pages.base_page import BasePage
from pages.inbox.modals.create_column import CreateColumnModal
from pages.inbox.modals.create_ticket_modal import CreateTicketModal
from playwright.sync_api import expect

class SideBar(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.btn_create_column = page.get_by_role("link", name="Crear columna")
        self.btn_create_column = page.locator(".modal-new-column i.fa-add")
        self.btn_create_ticket = page.locator(".dropdown .fa-ticket")
        self.btn_go_to_ticket = page.get_by_role("link", name="Ir a ticket")

    def open_new_column_modal(self):
        expect(self.btn_create_column).to_be_visible(timeout=10000)
        modal = CreateColumnModal(self.page)
        self.click_until_visible(self.btn_create_column, modal.container, max_retries=5)
        return modal

    def open_new_ticket_modal(self):
        expect(self.btn_create_ticket).to_be_visible(timeout=10000)
        modal = CreateTicketModal(self.page)
        self.click_until_visible(self.btn_create_ticket, modal.container, max_retries=5)
        return modal # es un componente(page), no es un locator