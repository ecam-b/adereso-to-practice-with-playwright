from pages.base_page import BasePage
from playwright.sync_api import expect

class CreateColumnModal(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.container = page.locator(".modal-content")
        self.input_name_column = self.container.get_by_placeholder("Nombre de la columna").filter(visible=True)
        self.btn_add = page.get_by_role("button", name="Añadir")
        self.btn_edit = page.get_by_role("button", name="Guardar")

    def wait_until_visible(self):
        expect(self.container).to_be_visible(timeout=10000)

    def submit_form(self, is_edit=False):
        """Hace click en el botón correcto según el contexto."""
        if is_edit:
            self.btn_edit.click()
        else:
            self.btn_add.click()

    def fill_and_save(self, name: str, is_edit=False):
        self.input_name_column.fill(name)
        self.submit_form(is_edit)