import aiohttp
import asyncio

async def handle(request):
    # ... your web server request handler ...
    return web.Response(text="Hello, world!")

async def start_server():
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000) # or a different port
    await site.start()
    print("Web server started on port 8000")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
