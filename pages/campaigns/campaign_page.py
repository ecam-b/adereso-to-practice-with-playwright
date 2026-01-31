from pages.base_page import BasePage
from pages.campaigns.new_campaign_page import NewCampaignPage
from pages.campaigns.components.campaign_row_component import CampaignRowComponent
from pages.components.globals.alert_component import AlertComponent
from playwright.sync_api import expect

class CampaignPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.iframe = page.frame_locator("#campaignsIframe")
        self.alert = AlertComponent(self.iframe)
        self.btn_create_campaign = self.iframe.get_by_role("button", name="Crear campaña")
        self.table_rows = self.iframe.locator("table tbody tr") #todas las rows

    def click_create_campaign(self):
        expect(self.btn_create_campaign).to_be_visible(timeout=30000)
        self.btn_create_campaign.click()

        return NewCampaignPage(self.page)

    def get_campaign_row(self, name: str) -> CampaignRowComponent:
        row_locator = self.table_rows.filter(has_text=name)
        return CampaignRowComponent(row_locator)