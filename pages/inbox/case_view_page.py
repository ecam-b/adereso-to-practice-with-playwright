from pages.inbox.components.column_component import ColumnComponent

class CaseViewPage:
    def __init__(self, page):
        self.page = page

        self.id_label = self.page.locator('.case-detail-badge._button')
        self.column_container = page.locator('.column-container')
        self.column = self.column_container.locator(".column")


    def get_id_label(self):
        return self.id_label ##retorna el localizador en vez de texto plano

    def get_column(self):
        return ColumnComponent(self.column)