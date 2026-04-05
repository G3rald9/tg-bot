import os
import asyncio
import httpx
from telegram import Bot

TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), os.getenv("CHAT_ID")
WALLET = "7s8Bdc4cdLfusLmCKjQfsGN3k6hFjn8GQ21h2x4nvBq"
bot = Bot(token=TOKEN)

async def main():
    last_tx = None
    async with httpx.AsyncClient() as client:
        while True:
            try:
                r = await client.get(f"https://public-api.solscan.io/account/transactions?address={WALLET}&limit=1")
                data = r.json()
                
                if data and data[0]['txHash'] != last_tx:
                    last_tx = data[0]['txHash']
                    await bot.send_message(CHAT_ID, "New transaction detected!")
            except Exception as e:
                print(f"Error: {e}") # This prevents the crash
            
            await asyncio.sleep(20) 

asyncio.run(main())
