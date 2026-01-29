from playwright.sync_api import Locator, expect

class ChatComponent:
    def __init__(self, root_locator: Locator):
        self.root = root_locator

        self.last_message = self.root.locator(".case-message-container").last

        self.date_creation = self.last_message.locator(".creation-date-and-status")
        self.first_check = self.date_creation.locator("i.fa-check").first

        self.last_message_image = self.last_message.locator('message-image[ng-repeat="image in message.media_set"]')

    def get_src_image_message(self) -> str:
        """Obtiene el src de la imagen del último mensaje"""
        expect(self.last_message_image).to_be_visible(timeout=10000)
        src = self.last_message_image.get_attribute('src')
        # Validar que no esté vacío
        assert src, "El atributo src está vacío"
        
        return src