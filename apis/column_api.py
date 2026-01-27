from apis.base_api import BaseAPI

class ColumnAPI(BaseAPI):
    def create_column(self, name: str, update_from_date: int = None):
        """Crea una columna"""
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
