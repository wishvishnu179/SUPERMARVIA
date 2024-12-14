import logging
import logging.config
import asyncio

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL, LOG_STR
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from Script import script
from aiohttp import web
from datetime import date, datetime
import pytz
from pyrogram import utils as pyroutils
pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999


class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username
        self.log_channel = LOG_CHANNEL
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(LOG_STR)
        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S %p")
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        # ... (Your iter_messages function remains unchanged) ...


app = Bot()
app_web = web.Application()
async def health_check(request):
    return web.Response(text='OK')

app_web.add_routes([web.get('/health', health_check)])

async def start_health_check():
    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8081)  #Use a different port than your main app
    await site.start()

async def run_health_check():
    loop = asyncio.get_running_loop()
    loop.run_until_complete(start_health_check())

    async def start(self):
        # Existing start code ...
        asyncio.create_task(run_health_check())  # Start the health check in the background

    async def stop(self, *args):
       # Shut down the health check
       await app_web.shutdown()
       await app_web.cleanup()
       await super().stop()
       logging.info("Bot stopped. Bye.")


app.run()
