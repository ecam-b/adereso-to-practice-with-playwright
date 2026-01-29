from playwright.sync_api import expect

class AlertComponent:
    def __init__(self, page):
        self.page = page
        self.container = page.locator(".alert-container")
        self.message_successfully_send = page.get_by_role("alert").filter(has_text="El mensaje privado fue enviado.")

    def wait_for_message(self, text: str, timeout=10000):
        expect(self.container).to_be_visible(timeout=timeout)
        expect(self.container).to_contain_text(text)

    def wait_for_success_send(self, timeout=10000):
        expect(self.message_successfully_send).to_be_visible(timeout=timeout)