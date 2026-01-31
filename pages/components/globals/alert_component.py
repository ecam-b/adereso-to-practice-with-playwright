from playwright.sync_api import expect

class AlertComponent:
    def __init__(self, page):
        self.page = page
        self.toast_container = page.locator(".Vue-Toastification__toast")
        self.message_successfully_send = page.get_by_role("alert").filter(has_text="El mensaje privado fue enviado.")

    def wait_for_toast(self, message: str, timeout: int = 5000):
        # Busca un toast visible que contenga el texto
        # Usamos locator genérico para mayor compatibilidad
        toast = self.page.locator(".Vue-Toastification__toast").filter(has_text=message)
        expect(toast).to_be_visible(timeout=timeout)

    def wait_for_success_send(self, timeout=10000):
        expect(self.message_successfully_send).to_be_visible(timeout=timeout)