from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.components.globals.alert_component import AlertComponent

from typing import Dict

class NewCampaignPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.iframe = page.frame_locator("#campaignsIframe")
        self.alert = AlertComponent(self.iframe)

        self.name_input = self.iframe.get_by_placeholder("Ingresa nombre de la campaña")
        self.account_select = self.iframe.get_by_placeholder("Selecciona tu cuenta de origen")
        self.hsm_select = self.iframe.get_by_placeholder("Selecciona una plantilla de mensaje HSM")
        self.upload_document_file = self.iframe.locator('input[type="file"]')
        self.name_file_upload = self.iframe.locator('.upload-box b')
        self.confirmation_check = self.iframe.get_by_role("checkbox", name="Confirmo que quienes recibirá")
        self.btn_create_campaign = self.iframe.get_by_role("button", name="Crear campaña")

    def select_account(self, account: str):
        self.account_select.click()
        self.iframe.get_by_text(account).click()
        
    def select_hsm(self, hsm: str):
        expect(self.hsm_select).to_be_enabled(timeout=10000)
        self.hsm_select.fill(hsm)
        option = self.iframe.get_by_text(hsm)
        option.wait_for(state="visible", timeout=5000)
        option.click()

    def upload_file(self, path: str):
        self.upload_document_file.set_input_files(path)

    def create_simple_campaign(self, name: str, account: str, hsm: str, path: Dict):
        self.name_input.fill(name)
        self.select_account(account)
        self.select_hsm(hsm)
        self.upload_file(path["path"])
        expect(self.name_file_upload).to_contain_text(path["name"], timeout=5000)
        self.check_and_create()
        self.alert.wait_for_toast("Campaña creada exitosamente", timeout=5000)

        from pages.campaigns.campaign_page import CampaignPage
        return CampaignPage(self.page)

    def check_and_create(self):
        self.confirmation_check.check()
        expect(self.btn_create_campaign).to_be_enabled()
        self.btn_create_campaign.click()