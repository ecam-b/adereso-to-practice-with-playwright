from playwright.sync_api import expect
from pages.campaigns.campaign_page import CampaignPage

class TopMenu():
    def __init__(self, page):
        self.page = page
        self.container = self.page.locator('[ng-if="config.showBar"]')
        self.menu_modules = self.container.locator('[uib-dropdown="uib-dropdown"]').filter(has_text="Módulos")
        self.opt_engage = self.menu_modules.locator("ul li").filter(has_text="Engage (Mis campañas)")

    def go_to_engage(self):
        expect(self.menu_modules)
        self.menu_modules.click()
        self.opt_engage.click()
        return CampaignPage(self.page)