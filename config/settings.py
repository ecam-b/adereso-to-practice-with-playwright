import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    URL = os.getenv("WEB_URL")
    USER = os.getenv("UI_USER")
    PASSWORD = os.getenv("UI_PASS")
    SIMPLE_HSM_TEXT = "qa_test_simple_text_1"