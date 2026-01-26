from pages.base_page import BasePage
from pages.inbox.components.sidebar import SideBar
from pages.components.globals.top_menu import TopMenu
from config.settings import Config
from pages.inbox.components.column_component import ColumnComponent


class InboxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sidebar = SideBar(page)
        self.topmenu = TopMenu(page)
        self.column_container = page.locator('.column-container')

    def navigate_to(self):
        self.navigate(f"{Config.URL}/#/inbox/")

    def get_column(self, name: str) -> ColumnComponent:
        # 1. Buscamos el contenedor raíz de esa columna específica
        column_locator = self.column_container.locator('.column').filter(has_text=name)
        # 2. Envolvemos ese locator en nuestra clase componente
        # Esto es lo que permite hacer: inbox.get_column("Ventas").open_options()
        return ColumnComponent(column_locator)