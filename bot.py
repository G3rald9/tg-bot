import os, asyncio, httpx
from telegram import Bot

TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), os.getenv("CHAT_ID")
WALLET = "7s8Bdc4cdLfusLmCKjQfsGN3k6hFjn8GQ21h2x4nvBq"
#
RPC_URL = "https://api.mainnet-beta.solana.com"

bot = Bot(token=TOKEN)

async def main():
    last_tx = None
    payload = {
        "jsonrpc": "2.0", "id": 1,
        "method": "getSignaturesForAddress",
        "params": [WALLET, {"limit": 1}]
    }

    async with httpx.AsyncClient() as client:
        print("Monitoring via Direct RPC...")
        while True:
            try:
                response = await client.post(RPC_URL, json=payload)
                data = response.json()
                
                # Solana RPC returns data in a 'result' list
                if "result" in data and len(data["result"]) > 0:
                    current_tx = data["result"][0]["signature"]
                    
                    if current_tx != last_tx:
                        if last_tx is not None:
                            await bot.send_message(CHAT_ID,  f"🚨 New Trx\n\nFrom:\n`{WALLET}`",
    parse_mode="Markdown")
                        last_tx = current_tx
            except Exception as e:
                print(f"Connection Error: {e}")
            
            await asyncio.sleep(15) 

asyncio.run(main())
