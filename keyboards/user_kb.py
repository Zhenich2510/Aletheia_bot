from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_start_and_help = KeyboardButton('/start')
button_hello_aletheia = KeyboardButton('/hello_aletheia')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(button_start_and_help, button_hello_aletheia)
