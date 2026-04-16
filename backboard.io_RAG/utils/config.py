import os
from dotenv import load_dotenv

load_dotenv()

BACKBOARD_API_KEY = os.getenv("BACKBOARD_API_KEY")

# Debugger (optional) 
DEBUG = os.getenv("DEBUG", "False") == "True"
APP_NAME = "Backboard Assistant"