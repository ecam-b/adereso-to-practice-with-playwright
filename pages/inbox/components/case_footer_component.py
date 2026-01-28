from playwright.sync_api import Locator

class CaseFooterComponent:
    def __init__(self, root_locator: Locator):
        self.root = root_locator

        self.account_selector = self.root.locator(".ad-reply-account-selector__selected-name-container")
        self.status_text_label = self.root.locator(".case-control__case-open-close")