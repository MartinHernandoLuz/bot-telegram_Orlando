from flask_env import MetaFlaskEnv
import os
from dotenv import load_dotenv
load_dotenv()

class Configuration(metaclass=MetaFlaskEnv):
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    NGROK_TOKEN = os.getenv("NGROK_TOKEN")
    NGROK_URL = os.getenv("NGROK_URL")
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    WEBHOOK = f"{NGROK_URL}/webhook"

    # Imprime las variables de entorno para verificar si están cargadas correctamente
    print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
    print("NGROK_TOKEN:", NGROK_TOKEN)
    print("NGROK_URL:", NGROK_URL)
    print("PORT:", PORT)
    print("DEBUG:", DEBUG)
    print("WEBHOOK:", WEBHOOK)