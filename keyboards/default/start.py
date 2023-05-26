from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh menyu"),
            KeyboardButton(text="Firma qo'shish"),
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
add_firma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Firma qo'shish"),
        ],
    ],
    resize_keyboard=True,
)