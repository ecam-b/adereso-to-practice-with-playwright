from playwright.sync_api import expect
from playwright.sync_api import Locator

class CaseFooterComponent:
    def __init__(self, root_locator: Locator):
        self.root = root_locator
        self.page = root_locator.page

        self.account_selector = self.root.locator(".ad-reply-account-selector__selected-name-container")
        self.status_text_label = self.root.locator(".case-control__case-open-close")

        self.textarea_reply = self.root.locator('textarea[name="text"]')
        self.input_file = self.root.locator('input[type="file"]')
        self.upload_document_file = self.root.locator('[ng-repeat="file in uploadedDocumentFiles"]')
        self.btn_send_reply = self.root.get_by_role("button", name="Enviar mensaje privado")


    def send_message_reply(self, msg: str):
        self.textarea_reply.fill(msg)
        expect(self.btn_send_reply).to_be_enabled(timeout=10000)
        self.btn_send_reply.click()
        expect(self.btn_send_reply).to_be_disabled(timeout=5000)
        return self

    def attach_and_send(self, msg: str, file_path: str):
        # inyectamos el archivo con .set_input_files()
        self.input_file.set_input_files(file_path) # playwright se encarga de todo
        expect(self.upload_document_file).to_be_visible(timeout=10000)
        self.textarea_reply.fill(msg)
        expect(self.btn_send_reply).to_be_enabled(timeout=10000)
        self.btn_send_reply.click()
        from pages.components.globals.alert_component import AlertComponent

        return AlertComponent(self.page)
        