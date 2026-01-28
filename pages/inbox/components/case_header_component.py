from playwright.sync_api import Locator

class CaseHeaderComponent:
    def __init__(self, root_locator: Locator):
        self.root = root_locator

        self.client_name = self.root.locator(".name")
        self.id_label = self.root.locator('.case-detail-badge._button')
        self.client_phone = self.root.locator('span[ng-if="vm.userObject.uname"]')