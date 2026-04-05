import requests
import os
from telegram import Bot
import asyncio

#credentials


TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WALLET = "7s8Bdc4cdLfusLmCKjQfsGN3k6hFjn8GQ21h2x4nvBq"

bot = Bot(token=TOKEN)
last_tx = None

async def main():
    global last_tx

    while True:
        url = f"https://public-api.solscan.io/account/transactions?address={WALLET}&limit=1"
        data = requests.get(url).json()

        if data:
            tx = data[0]['txHash']

            if tx != last_tx:
                last_tx = tx
                await bot.send_message(chat_id=CHAT_ID, text="New transaction detected!")

        await asyncio.sleep(10)

asyncio.run(main())
