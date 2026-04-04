import os
import asyncio
from telegram import Bot

# Fetching credentials
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Initialize the bot
bot = Bot(token=TOKEN)

async def main():
    running = True
    print("Starting loop...")
    
    while running:
        # Use 'await' to ensure the message is actually sent
        await bot.send_message(chat_id=CHAT_ID, text="Running...")
        
        # Use asyncio.sleep instead of time.sleep in async functions
        await asyncio.sleep(3)

if __name__ == "__main__":
    # This starts the asynchronous event loop
    asyncio.run(main())
