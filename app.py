from aiogram import executor
import asyncio
from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    await db.create()
async def myFunc():
    await db.create()


if __name__ == '__main__':

    executor.start_polling(dp, on_startup=on_startup)
    #asyncio.run(myFunc())
