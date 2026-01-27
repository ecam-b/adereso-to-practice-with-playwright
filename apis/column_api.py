

class ColumnAPI:
    def __init__(self, request_context):
        self.request = request_context
        self.base_url = "https://apicaulifla.adere.so"

    def login(self, username: str, password: str, response_user: str):
        payload = {
            "username": username,
            "password": password,
            "response_user": response_user
        }
        response = self.request.post(f"{self.base_url}/api/v1/login/", data=payload) # esta es la linea de la petición post
        assert response.ok, f"Error al realizar el login: {response.text}"
        # guardar token internamente
        self.token = f"Token {response.json()["token"]}"
        return self.token

    def _get_headers(self):
        if not self.token:
            raise ValueError("Debes hacer el login primero con api.login()")
        return {"Authorization": self.token}

    def create_column(self, name: str, update_from_date: int = None):
        if update_from_date is None:
            import time
            update_from_date = int(time.time()) - (30 * 24 * 60 * 60)

        payload = {
            "name": name,
            "column_type": "case",
            "social_networks": ["whatsapp"],
            "pagination_field": "updated_time",
            "updated_from_date": update_from_date,
            "ticket_export": True,
            "message_export": True,
            "client_export": True,
            "comment_export": True
        }
        response = self.request.post(
            f"{self.base_url}/api/v1/columns/", 
            data=payload,
            headers=self._get_headers()
            )
        assert response.ok, f"Error al crear columna: {response.text}"
        return response.json()

    def delete_column(self, column_id: str):
        response = self.request.delete(
            f"{self.base_url}/api/v1/column/{column_id}/",
            headers=self._get_headers()
            )
        assert response.ok, f"Error al eliminar columna: {response.text}"

    def create_ticket(self, simple_hsm, bsp_id, phone_client):
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
            headers=_get_headers()
        )
        assert response.ok, f"Error al crear ticket: {response.text}"
        return response.json()
