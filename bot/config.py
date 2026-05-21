import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")

settings = Settings()