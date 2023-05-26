from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh menyu"),
        ],
    ],
    resize_keyboard=True,
)

register = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ro'yxatdan o'tish"),
        ],
    ],
    resize_keyboard=True,
)