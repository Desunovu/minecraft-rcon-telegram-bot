import logging, os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

# .env
load_dotenv()

API_TOKEN = os.environ.get('TG_API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

from rconclient.bot_cmd import *


def start_bot():
    executor.start_polling(dp, skip_updates=True)



