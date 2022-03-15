from aiogram.utils import executor

from start_bot import dp
from start_bot import on_startup
from handlers import other, user, admin
from database import start_db

def main():
    start_db()
    user.register_handlers_user(dp)
    admin.register_handlers_admin(dp)
    # other.register_handlers_other(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    pass


if __name__ == '__main__':
    main()
