from playwright.sync_api import Locator

class ChatComponent:
    def __init__(self, root_locator: Locator):
        self.root = root_locator

        self.last_message = self.root.locator(".case-message-container").last
        self.date_creation = self.last_message.locator(".creation-date-and-status")
        self.first_check = self.date_creation.locator("i.fa-check").first