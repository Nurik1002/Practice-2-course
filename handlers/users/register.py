from aiogram import types
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from states.user_state import RegisterState
import re


@dp.message_handler(text="Ro'yxatdan o'tish")
async def royxatdan_otish(msg:Message):
    await msg.answer("Iltimos famliya va ismingizni kiriting! Namuna (Familiya Ism) : ")
    await RegisterState.full_name.set()

@dp.message_handler(state=RegisterState.full_name)
async get_full_name(msg : Message, state : FSMContext):

    try:
        last_name, first_name = msg.text.split()
        await state.update_data({
            "last_name" : last_name,
            "fist_name" : first_name
        })
        await msg.answer("Iltimos email manzilingizni kiriting! Namuna 'nyarashbayev97@gmail.com'")
        await RegisterState.email.set()

    except:
        await msg.answer("Iltimos familiya va ismingizni to'g'ri kiriting. Namuna 'Yarashbayev Nurgeldi'")



@dp.message_handler(state=RegisterState.email)
async get_email(msg : Message, state : FSMContext):
    email = msg.text
    if re.match(r"[\w]*@*[a-z]*\.*[\w]{5,}(\.)*(com)*(@gmail\.com)", email):
        await state.update_data({
            "email" : email
        })
        await RegisterState.phone_num.set()
        await msg.anwer("Iltimos bog'lainish uchun telefon raqamingzini kiriting! Namuna '913169659'")
    else:
        await msg.answer("Iltimos email manzilingizni to'g'ri kiriting! Namuna 'nyarashbayev97@gmail.com'")
    
@dp.message_handler(state=RegisterState.phone_num)

@dp.message_handler(state=RegisterState.manzil)

