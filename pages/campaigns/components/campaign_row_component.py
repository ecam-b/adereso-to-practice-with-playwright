from playwright.sync_api import Locator
import re

class CampaignRowComponent:
    def __init__(self, root_locator: Locator):
        self.root = root_locator
        self.page = root_locator.page

        self.btn_send = self.root.locator("button.a-button-green")
        self.status_cell = self.root.locator("td").filter(has_text=re.compile(r"Enviando|Cargada|Error|Terminada", re.IGNORECASE))

    def send(self):
        self.btn_send.click()

    def get_status(self):
        return self.status_cell
