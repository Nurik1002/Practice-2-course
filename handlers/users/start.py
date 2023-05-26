from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start import register
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    telegram_id=message.from_user.id
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\nOnlayn do'konimizga tashrifingizdan minnatdormiz!!!")
    await message.answer(f"Botdan foydalanishingiz uchun ro'yxatdan o'tishingiz kerak. Iltimos 'Ro'yxatdan o'tish' tugmasini bo'sing!", reply_markup=register)
