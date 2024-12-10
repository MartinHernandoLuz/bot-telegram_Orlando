from flask_env import MetaFlaskEnv
import os

class Configuration(metaclass=MetaFlaskEnv):
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    NGROK_TOKEN = os.getenv("NGROK_TOKEN")
    NGROK_URL = os.getenv("NGROK_URL")
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    WEBHOOK = f"{NGROK_URL}/webhook"