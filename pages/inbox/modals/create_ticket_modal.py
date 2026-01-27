from playwright.sync_api import expect

class CreateTicketModal:
    def __init__(self, page):
        self.page = page
        self.container = self.page.locator("#case-add-form")
        self.account_select = self.container.locator('select[name="account"]')
        self.department_select = self.container.locator('select[name="department"]')
        self.hsm_select = self.container.locator('select[name="content"]')
        self.client_input = self.container.get_by_placeholder("Teléfono. Ejemplo +56 11111111 ")
        self.btn_send_message = self.container.get_by_role("button", name="Enviar mensaje")

    def wait_until_visible(self):
        expect(self.container).to_be_visible(timeout=10000)

    def select_origin_account(self, account_name: str):
        self.account_select.locator("option.ng-binding").first.wait_for(state="attached")
        
        self.account_select.select_option(label=account_name)

    def select_department(self, department_name: str):
        self.department_select.locator("option.ng-binding").first.wait_for(state="attached")
        
        self.department_select.select_option(label=department_name)

    def select_hsm(self, hsm_name: str):
        self.hsm_select.wait_for(state="attached")
        self.hsm_select.locator("option").first.wait_for(state="attached")
        
        self.hsm_select.select_option(label=hsm_name)

    def creat_new_ticket(self, account_name: str, department_name: str, hsm_name: str, number_phone: str):
        self.select_origin_account(account_name)
        self.select_department(department_name)
        self.select_hsm(hsm_name)
        self.client_input.fill(number_phone)
        expect(self.btn_send_message).to_be_enabled()
        self.btn_send_message.click()

        from pages.components.globals.ticket_creation_alert_component import TicketCreationAlertComponent
        return TicketCreationAlertComponent(self.page)