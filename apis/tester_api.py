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

    def get_identifier_from_ticket_id(self, ticket_id: str):
        response = self.request.get(f"{self.base_url}/api/v1/case/{ticket_id}", headers=self._get_headers())
        assert response.ok, f"Error al obtener el mensaje mediante id: {response.text}"
        return response.json()["identifier"]

    def close_ticket(self, ticket_id: str):
        payload = {
            "workflow_status": {
                "resource_id": "5e864f1c685e005577f05a91",
                "client_id": 1,
                "kind": 1,
                "category": 2,
                "core": True,
                "label": "Cerrado",
                "index": 2,
                "deleted": False,
                "created": "1585860380"
            },
            "is_closed": True
        }
        response = self.request.put(
            f"{self.base_url}/api/v1/case/{ticket_id}/",
            data=payload,
            headers=self._get_headers()
        )
        assert response.ok, f"Error al cerrar ticket: {response.text}"
        return response.json()