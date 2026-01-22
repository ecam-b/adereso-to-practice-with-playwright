from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.get_by_placeholder("Ej: Nombre@empresa.com")
        self.password_input = page.get_by_placeholder("Tu contraseña")
        self.btn_login = page.get_by_role("button", name="Iniciar sesión")
        # iframe
        self.recaptcha_frame = page.frame_locator("iframe[src*='google.com/recaptcha/api2/anchor'][src*='size=normal']")
        self.recaptcha_checkbox = self.recaptcha_frame.locator("span[id='recaptcha-anchor']")

    def login(self, user, password):
        self.username_input.fill(user)
        self.password_input.fill(password)
        self.btn_login.click()
        self.recaptcha_checkbox.click()
