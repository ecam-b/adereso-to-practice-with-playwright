from pages.inbox.components.column_component import ColumnComponent
from pages.inbox.components.right_sidebar import RightSideBar
from pages.inbox.components.case_header_component import CaseHeaderComponent
from pages.inbox.components.case_footer_component import CaseFooterComponent
from pages.inbox.components.chat_component import ChatComponent
from config.settings import Config

class CaseViewPage:
    def __init__(self, page):
        self.page = page

        self.sidebar_root = page.locator(".case-side-view__menu")
        self.column_container = page.locator('.column-container')
        self.header_root = self.page.locator(".case-detail-header")
        self.chat_root = self.page.locator(".case-messages__body")
        self.footer_root = self.page.locator(".case-messages__footer")

        self.right_sidebar = RightSideBar(self.sidebar_root)
        self.header = CaseHeaderComponent(self.header_root)
        self.chat = ChatComponent(self.chat_root)
        self.footer = CaseFooterComponent(self.footer_root)

        self.column = self.column_container.locator(".column")

    def get_column(self):
        return ColumnComponent(self.column)

    def go_to_ticket(self, ticket_id: str):
        self.page.goto(f"{Config.URL}/#/inbox/case/{ticket_id}/")