from playwright.sync_api import expect

class AlertComponent:
    def __init__(self, page):
        self.page = page
        self.container = page.locator(".alert-success")

    def wait_for_message(self, text: str, timeout=10000):
        expect(self.container).to_be_visible(timeout=timeout)
        expect(self.container).to_contain_text(text)