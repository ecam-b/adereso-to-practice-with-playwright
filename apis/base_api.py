from config.settings import Config

class BaseAPI:
    def __init__(self, request_context):
        self.request = request_context
        self.base_url = Config.URL
        self.token = None
    
    def login(self, username: str, password: str, response_user: str = "true"):
        """Realiza login y guarda el token internamente"""
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
        """Retorna los headers con autorización"""
        if not self.token:
            raise ValueError("Debes hacer el login primero con api.login()")
        return {"Authorization": self.token}