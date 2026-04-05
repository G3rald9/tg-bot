import os
import asyncio
from telegram import Bot

# credentials
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Initialize bot
bot = Bot(token=TOKEN)

async def main():
    running = True
    print("Starting loop...")
    
    while running:
    
        await bot.send_message(chat_id=CHAT_ID, text="Running...")
        
    
        await asyncio.sleep(3600)

if __name__ == "__main__":
    #Asynchronous  loop
    asyncio.run(main())
