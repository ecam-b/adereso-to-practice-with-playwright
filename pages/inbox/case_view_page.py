class CaseViewPage:
    def __init__(self, page):
        self.page = page

        self.id_label = self.page.locator('.case-detail-badge._button')

    def get_id_label(self):
        return self.id_label ##retorna el localizador en vez de texto plano