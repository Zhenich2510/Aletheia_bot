from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage


TOKEN = '5284633395:AAGcr0Fuqw1pRi2NEDIzmYfidmNmjGpYrQU'

storage = MemoryStorage()

async def on_startup(_):
    print('Bot online.')


bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)

