import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BACKBOARD_API_KEY = os.getenv("BACKBOARD_API_KEY")

    DEBUG = os.getenv("DEBUG", "False") == "True"
    APP_NAME = "Backboard Assistant"