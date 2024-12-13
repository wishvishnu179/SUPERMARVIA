import logging
import logging.config
import threading
from flask import Flask
from pyrogram import Client

# ... (Your logging configuration remains the same) ...

from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL, LOG_STR

app = Client(
  name=SESSION,
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  workers=50,
  plugins={"root": "plugins"},
  sleep_threshold=5,
)

flask_app = Flask(__name__)

@flask_app.route("/")
def health_check():
    return "OK"


def run_flask():
    flask_app.run(host='0.0.0.0', port=8000, debug=False, threaded=True)


@app.on_message() # Example handler, replace with your logic
async def echo(client, message):
    await message.reply(message.text)

async def main():
    await app.start()
    logging.info("Bot started")
    thread = threading.Thread(target=run_flask)
    thread.daemon = True
    thread.start()
    await app.idle() # Keep the bot running continuously

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
