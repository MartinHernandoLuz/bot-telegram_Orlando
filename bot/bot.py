from flask import Flask, request
import telebot
from bot.config import Configuration
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
bot = telebot.TeleBot(Configuration.TELEGRAM_TOKEN)

@app.route('/', methods=['GET'])
def index():
    return {
        "status": "Bot está corriendo",
        "webhook_url": Configuration.WEBHOOK_URL,
        "environment": os.getenv("FLASK_ENV", "production"),
    }


@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    if json_data:
        bot.process_new_updates([telebot.types.Update.de_json(json_data)])
    return "OK", 200


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola, ¿cómo puedo ayudarte?")


@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    user = message.new_chat_members[0]
    bot.send_message(
        message.chat.id,
        f"👋 ¡Hola **{user.first_name}**! 🎉\n\n"
        f"🤖 Bienvenido al **Grupo FullStacks** 🚀\n\n"
        f"💡 Aquí compartimos conocimientos, ideas y aprendemos juntos sobre programación y desarrollo. \n\n"
        f"✅ **Reglas básicas**:\n"
        f"- Mantén el respeto entre los miembros. 🙏\n"
        f"- Comparte tus dudas o conocimientos, siempre serán bienvenidos. 💬\n\n"
        f"¡Esperamos que disfrutes de tu estadía y aprendas mucho! 🧑‍💻✨"
    )