from playwright.sync_api import expect
from pages.inbox.case_view_page import CaseViewPage
from config.settings import Config

class TicketCreationAlertComponent:
    def __init__(self, page):
        self.page = page
        self.container = self.page.locator('.alert-success:has-text("HSM enviado exitosamente")')
        self.link_ticket = self.container.get_by_role("link", name="Ir al ticket")

    def wait_until_visible(self):
        expect(self.container).to_be_visible()

    def go_to_new_ticket(self) -> CaseViewPage:
        href = self.link_ticket.get_attribute("href")
        ticket_id = href.split("/")[-2]
        # navegar al case view del ticket
        self.page.goto(f"{Config.URL}/#/inbox/case/{ticket_id}/")
        return CaseViewPage(self.page)