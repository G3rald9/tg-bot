import os
import time
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

running = True

while running:
    bot.send_message(chat_id=CHAT_ID, text="Running...")
    time.sleep(3)
