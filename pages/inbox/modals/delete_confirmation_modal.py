from pages.base_page import BasePage

class DeleteConfirmationModal(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.container = page.locator(".modal-dialog")
        self.btn_cancel = self.container.get_by_role("button", name="Cancelar")
        self.btn_confirm_delete = self.container.get_by_role("button", name="Eliminar columna")

    def confirm_deletion(self):
        self.btn_confirm_delete.click()

        from pages.inbox.inbox_page import InboxPage
        return InboxPage(self.page)
    
    def cancel_deletion(self):
        self.btn_cancel.click()

        from pages.inbox.inbox_page import InboxPage
        return InboxPage(self.page)