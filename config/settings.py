import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    URL = os.getenv("WEB_URL")
    USER = os.getenv("UI_USER")
    PASSWORD = os.getenv("UI_PASS")
    ACCOUNT = "Adereso BSP One (56949591142)"
    ACCOUNT_NAME = "Adereso BSP One"
    BSP_ID = "315"
    DEPARTMENT = "Sin departamento"
    SIMPLE_HSM_TEXT = "qa_test_simple_text_1"
    CONTAIN_SIMPLE_HSM_TEXT = "Cordial saludo estimado usuario, esta es una prueba de comunicacion desde la seccion (Sin Departamento). Que tenga un gran dia."
    PHONE = "573115734967"
    CLIENT_NAME = "Elian"