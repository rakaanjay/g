from lib.driver.stream import app
from pyrogram import Client, idle
from lib.config import API_HASH, API_ID, BOT_TOKEN

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="lib.driver"),
)

bot.start()
app.start()
idle()
