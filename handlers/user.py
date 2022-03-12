from aiogram import types
from aiogram.dispatcher import Dispatcher

from conf import cmd_start_and_help_text, cmd_hello_aletheia_text_1, cmd_hello_aletheia_text_2

from start_bot import bot
from keyboards import kb_client

# @dp.message_handler(commands=['start', 'help'])
async def cmd_start_and_help(message: types.Message):
    await bot.send_message(message.from_user.id, cmd_start_and_help_text)

# @dp.message_handler(commands=['kb'])
async def cmd_kb(message: types.Message):
    await bot.send_message(message.from_user.id,'Увімкнула кнопки',  reply_markup=kb_client)

# @dp.message_handler(commands='hello_aletheia')
async def cmd_hello_aletheia(message: types.Message):
    await bot.send_message(message.from_user.id, cmd_hello_aletheia_text_1 + str(message.from_user.username) + cmd_hello_aletheia_text_2)

def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(cmd_start_and_help, commands=['start', 'help'])
    dp.register_message_handler(cmd_hello_aletheia, commands='hello_aletheia')
    dp.register_message_handler(cmd_kb, commands=['kb'])
