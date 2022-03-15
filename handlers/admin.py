from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from start_bot import bot
from database import add_info_to_db
from conf import cmd_admin_text, cmd_load_text, get_conclusion_text, cmd_stop_text

ID = None
admins = 431687242
data = {}


class FSMAdmin(StatesGroup):
    news_text = State()
    conclusion = State()


# @dp.message_handler('admin')
async def cmd_admin(message: types.Message):
    global ID
    ID = message.from_user.id
    if ID == admins:
        await bot.send_message(message.from_user.id, cmd_admin_text)
        await message.delete()


# @dp.message_handler('load', state=None)
async def cmd_load(message: types.Message):
    if ID == message.from_user.id:
        await FSMAdmin.news_text.set()
        await bot.send_message(message.from_user.id, cmd_load_text)


# @dp.message_handler('stop', state='*')
async def cmd_stop(message: types.Message, state: FSMContext):
    if ID == message.from_user.id:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply(cmd_stop_text)


# @dp.message_handler(state=FSMAdmin.news_text)
async def get_text(message: types.Message, state: FSMContext):
    if ID == message.from_user.id:
        data['user_id'] = message.from_user.id
        data['user_nickname'] = message.from_user.username
        data['user_text'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, get_conclusion_text)


# @dp.message_handler(state=FSMAdmin.news_text)
async def get_conclusion(message: types.Message, state: FSMContext):
    if ID == message.from_user.id:
        if message.text == '1':
            data['predict'] = True
        elif message.text == '0':
            data['predict'] = False
        add_info_to_db(data['user_id'], data['user_nickname'], data['user_text'], data['predict'])
        await message.reply('Done')
        await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cmd_admin, commands='admin')
    dp.register_message_handler(cmd_load, commands='load', state=None)
    dp.register_message_handler(cmd_stop, commands='stop', state="*")
    dp.register_message_handler(get_text, state=FSMAdmin.news_text)
    dp.register_message_handler(get_conclusion, state=FSMAdmin.conclusion)
