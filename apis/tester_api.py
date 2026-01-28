from apis.base_api import BaseAPI

class TesterAPI(BaseAPI):
    def send_message_by_tester(self, account_number: str, message: str, user_uid: str = "user_playwright", social_network: str = "whatsapp"):
        payload = {
            "account_uid": account_number,
            "social_network": social_network,
            "user_uid": user_uid,
            "message": message,
            "inbound": True,
            "attachments": []
        }
        response = self.request.post(
            f"{self.base_url}/api/v2/tester/messages/",
            data=payload,
            headers = self._get_headers()
        )
        assert response.ok, f"Error enviar mensaje mediante tester: {response.text}"
        return response.json()["ticket_id"]