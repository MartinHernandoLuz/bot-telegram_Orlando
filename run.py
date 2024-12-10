import os
import subprocess
from dotenv import load_dotenv
from bot.bot import app
from bot.config import Configuration
import telebot
import time

load_dotenv()

if __name__ == "__main__":
    env = os.getenv("ENV", "production").lower()

    # Inicia ngrok y obtiene la URL
    print("Iniciando ngrok...")
    ngrok_command = [
        "ngrok", "tunnel",
        "--label", "edge=edghts_2iwEKxxH9cNK7AT3xpBJwSvpxGI",
        f"http://localhost:{Configuration.PORT}"
    ]
    ngrok_process = subprocess.Popen(ngrok_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Espera unos segundos para que ngrok genere la URL
    time.sleep(5)

    # Verifica si NGROK_URL está disponible
    ngrok_url = os.getenv("NGROK_URL")
    if not ngrok_url:
        print("Error: NGROK_URL no está definido en el entorno. Por favor verifica ngrok.")
        ngrok_process.terminate()
        exit(1)

    # Configuración del bot
    Configuration.WEBHOOK = f"{ngrok_url}/webhook"
    print(f"Webhook URL: {Configuration.WEBHOOK}")

    bot = telebot.TeleBot(Configuration.TELEGRAM_TOKEN)

    if env == "development":
        print("Running in development mode...")
        app.run(host="0.0.0.0", port=Configuration.PORT, debug=Configuration.DEBUG)
    else:
        print("Running in production mode...")
        bot.remove_webhook()
        bot.set_webhook(url=Configuration.WEBHOOK)
        app.run(host="0.0.0.0", port=Configuration.PORT, debug=Configuration.DEBUG)

