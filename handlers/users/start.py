
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start import register, menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    telegram_id=message.from_user.id
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\nOnlayn do'konimizga tashrifingizdan minnatdormiz!!!")

    chek_result = await db.chek_user(telegram_id=telegram_id)
    if chek_result == '1':
        await message.answer("Mahsulotlarni ko'rish uchun 'Bosh menyu' tugmasini bosing!", reply_markup=menu)

    elif chek_result == '0':
        await message.answer(f"Botdan foydalanishingiz uchun ro'yxatdan o'tishingiz kerak. Iltimos 'Ro'yxatdan o'tish' tugmasini bo'sing!", reply_markup=register)
