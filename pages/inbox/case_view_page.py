from pages.inbox.components.column_component import ColumnComponent
from pages.inbox.components.right_sidebar import RightSideBar

class CaseViewPage:
    def __init__(self, page):
        self.page = page
        sidebar_root = page.locator(".case-side-view__menu")
        self.right_sidebar = RightSideBar(sidebar_root)

        self.column_container = page.locator('.column-container')
        self.column = self.column_container.locator(".column")

        # header
        self.header = self.page.locator(".case-detail-header")
        self.client_name = self.header.locator(".name")
        self.id_label = self.header.locator('.case-detail-badge._button')
        self.client_phone = self.header.locator('span[ng-if="vm.userObject.uname"]')

        # body messages
        self.messages_container = self.page.locator(".case-messages__body")
        self.last_message = self.messages_container.locator(".case-message-container").last
        self.date_creation = self.last_message.locator(".creation-date-and-status")
        self.first_check = self.date_creation.locator("i.fa-check").first

        # footer
        self.footer = self.page.locator(".case-messages__footer")
        self.account_selector = self.page.locator(".ad-reply-account-selector__selected-name-container")
        self.status_text_label = self.footer.locator(".case-control__case-open-close")




    def get_id_label(self):
        return self.id_label ##retorna el localizador en vez de texto plano

    def get_column(self):
        return ColumnComponent(self.column)