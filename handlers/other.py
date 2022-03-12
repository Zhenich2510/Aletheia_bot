from aiogram import types, Dispatcher
from start_bot import dp

# @dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo)
