import logging
import logging.config
import asyncio

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)

# ... (Your imports remain unchanged) ...

class Bot(Client):
    def __init__(self): # ... (Your __init__ method remains unchanged) ...
        
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
    site = web.TCPSite(runner, '0.0.0.0', 8081)
    await site.start()

async def run_health_check():
    loop = asyncio.get_running_loop()
    loop.run_until_complete(start_health_check())

async def run_bot():
    await app.run()

async def main():
    await asyncio.gather(app.start(), run_health_check(), run_bot())

if __name__ == "__main__":
    asyncio.run(main())
