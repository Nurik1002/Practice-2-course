
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start import register, menu, add_firma
from loader import dp, db
import logging

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    telegram_id=message.from_user.id
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\nOnlayn do'konimizga tashrifingizdan minnatdormiz!!!")

    chek_result = await db.check_user(telegram_id=telegram_id)
    logging.info(f"check_result in start.py {chek_result}")
    if str(chek_result) == '1':
        await message.answer("Mahsulotlarni ko'rish uchun 'Bosh menyu' tugmasini bosing!", reply_markup=menu)

    elif str(chek_result) == '0':
        await message.answer(f"Botdan foydalanishingiz uchun ro'yxatdan o'tishingiz kerak. Iltimos 'Ro'yxatdan o'tish' tugmasini bo'sing!", reply_markup=register)
