from playwright.sync_api import Locator

class TicketComponent:
    def __init__(self, root_locator: Locator):
        self.root = root_locator
        self.page = root_locator.page

        self.id_label = self.root.locator(".case-id-number")
        self.subjet_label = self.root.locator(".last-content")
        
        self.status_button = self.root.locator(".case-control__case-open-close")
        self.status_text_label = self.status_button.locator(".ladda-label")

    def open_detail(self):
        self.root.click()
        # Aquí encadenaríamos con la página del detalle del ticket
        from pages.inbox.case_view_page import CaseViewPage
        return CaseViewPage(self.page)

    def get_id(self) -> str:
        return self.id_label.inner_text().strip()

    def get_ticket_status(self) -> Locator:
        return self.status_text_label