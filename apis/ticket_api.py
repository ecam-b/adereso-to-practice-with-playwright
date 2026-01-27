from apis.base_api import BaseAPI

class TicketAPI(BaseAPI):
    def create_ticket(self, simple_hsm: str, bsp_id: str, phone_client: str):
        """Crea un ticket proactivo"""
        payload = {
            "hsmFlag": True,
            "sn": "whatsapp",
            "content": simple_hsm,
            "hsm_parameters": [],
            "hsm_count": 1,
            "account": { 
                "id": bsp_id,
                "sn": "whatsapp"
            },
            "user": {
                "name": f"+{phone_client}",
                "phone_number": f"+{phone_client}"
            }
        }
        response = self.request.post(
            f"{self.base_url}/api/v1/cases/new/",
            data=payload,
            headers=self._get_headers()
        )
        assert response.ok, f"Error al crear ticket: {response.text}"
        return response.json()

    def get_ticket_identifier(self, ticket_id: str):
        response = self.request.get(
            f"{self.base_url}/api/v1/case/{ticket_id}",
            headers=self._get_headers()
        )
        assert response.ok, f"Error al obtener información del ticket: {response.text}"
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